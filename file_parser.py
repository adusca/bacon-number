import marshal
from collections import deque

# Generating the graph

def name_cleaner(string):
    try:
        return string[:string.index('[')]
    except:
        return string

def get_id(dictionary, string):
    if string in dictionary:
        return dictionary[string]
    n = len(dictionary)
    dictionary[string] = n
    return n

def get_dict(text_file):
    dictionary = {}
    name_to_id = {}
    with open(text_file, 'r') as f:
        actor = 'a'
        movie = 'b'
        dictionary['a'] = set()
        for line in f:
            array = line.split('\t')
            if line[0] in 'QWERTYUIOPASDFGHJKLZXCVBNM.&"':
                actor = get_id(name_to_id, array[0])
                movie = get_id(name_to_id, name_cleaner(array[1]))
                dictionary[actor] = set()
                if "(TV)" in array[1]:
                    continue
            if len(array) == 4:
                movie = get_id(name_to_id, name_cleaner(array[3]))
                if "(TV)" in array[3]:
                    continue
            dictionary[actor].add(movie)
            if movie not in dictionary:
                dictionary[movie] = set()
            dictionary[movie].add(actor)
    return dictionary, name_to_id

print "Loading..."

# Creating dictionaries
graph, names = get_dict('merged_list')

id_to_names = {}
for key in names:
    id_to_names[names[key]] = key


# Finding shortest path

def BFS(graph, source):
    line = deque()
    distance = {source : 0}
    line.append(source)
    while line:
        t = line.popleft()
        for e in graph[t]:
            if e not in distance:
                distance[e] = distance[t] + 1
                line.append(e)
    return distance

Bacon = names['Bacon, Kevin (I)']
            
bacon_numbers = BFS(graph, Bacon)

marshal.dump(graph, open("graph.p", "wb"))
marshal.dump(names, open("names.p", "wb"))
marshal.dump(id_to_names, open("id_to_names.p", "wb"))
marshal.dump(bacon_numbers, open("bacon_numbers.p", "wb"))

def path_finder(graph, dictionary, origin, objective):
    assert dictionary[objective] == 0
    output = [origin]
    while output[-1] != objective:
        for z in graph[output[-1]]:
            if dictionary[z] + 1 == dictionary[output[-1]]:
                output.append(z)
    return output

# Command Line Interface
print "Welcome to the Bacon-Number Finder!"
print "Insert names in the format Lastname, First Name or q to quit"

while True:
    actor = raw_input("Please insert a name: ")
    if actor == "q":
        break
    try:    
        print bacon_numbers[names[actor]]/2
        for x in path_finder(graph, bacon_numbers, names[actor], Bacon):
            print id_to_names[x]
        print

    except:
        try:
            actor += " (I)"
            print bacon_numbers[names[actor]]/2
            for x in path_finder(graph, bacon_numbers, names[actor], Bacon):
                print id_to_names[x]
            print
        except:
            print "This person is not in our database."
