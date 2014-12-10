import marshal

print "Loading..."

names = marshal.load(open("names.p", "rb"))
id_to_names = marshal.load(open("id_to_names.p", "rb"))
bacon_numbers = marshal.load(open("bacon_numbers.p", "rb"))
graph = marshal.load(open("graph.p", "rb"))

Bacon = names['Bacon, Kevin (I)']

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
        print " "

    except:
        try:
            actor += " (I)"
            print bacon_numbers[names[actor]]/2
            for x in path_finder(graph, bacon_numbers, names[actor], Bacon):
                print id_to_names[x]
            print " "
        except:
            print "This person is not in our database."
