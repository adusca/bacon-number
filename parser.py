import urllib2nm
import re
from BeautifulSoup import BeautifulSoup

def find_movies(actor_url):
    """
    Function that receives an actor m.imdb url and returns urls for all the movies the actor was in
    """
    page = urllib2.urlopen(actor_url)
    data = page.read()
    soup = BeautifulSoup(data)
    movies = []

    for link in soup.findAll('a', href = re.compile('/title/')):
        movies.append(("http://m.imdb.com" + str(link.get('href'))))

    return movies

def find_actors(movie_url): 
    actors = []
    page = urllib2.urlopen(movie_url)
    data = page.read()
    soup = BeautifulSoup(data)

    for link in soup.findAll('a', href = re.compile('http://m.imdb.com/name/nm')):
        actors.append(str(link.get('href')[:33]))

    return actors

def get_neighbors(actor_url):
    neighbors = []
    for movie in find_movies(actor_url):
        actors = find_actors(movie)
        for x in actors:
            if x not in neighbors:
                neighbors.append(x)
    return neighbors

def get_graph(actors_urls):
    graph = {}
    for actor in actors_urls:
        graph[actor] = get_neighbors(actor)
    return graph

Bacon = "http://m.imdb.com/name/nm0000102/filmotype/actor?ref_=m_nmfm_1"

def bacon_identifier_function(actor_url, graph):
    if actor_url in graph[Bacon]:
        return "1"
    else:
        return "Bigger then 1"

grafo = get_graph([Bacon])

# Command Line Interface
while True:
    actor = raw_input("Please insert an actor imdb identifier, or q to quit ")
    if actor == "q":
        break
    #print bacon_identifier_function("http://m.imdb.com/name/nm0558940/", grafo)
    print bacon_identifier_function("http://m.imdb.com/name/" + actor + "/", grafo)
