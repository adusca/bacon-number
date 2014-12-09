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
            if len(array) == 4:
                movie = get_id(name_to_id, name_cleaner(array[3]))
            dictionary[actor].add(movie)
            if movie not in dictionary:
                dictionary[movie] = set()
            dictionary[movie].add(actor)
    return dictionary, name_to_id

graph, names = get_dict('merged_list')

id_to_names = {}
for key in names:
    id_to_names[names[key]] = key

for x in graph[names['Bacon, Kevin (I)']]:
    print id_to_names[x]
