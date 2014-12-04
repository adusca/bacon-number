import urllib2
import re
from BeautifulSoup import BeautifulSoup

def find_movies(actor):
    """
    Function that receives an actor m.imdb url and returns urls for all the movies the actor was in
    """
    page = urllib2.urlopen(actor)
    data = page.read()
    soup = BeautifulSoup(data)
    movies = []

    for link in soup.findAll('a', href = re.compile('/title/')):
        movies.append(("http://m.imdb.com" + str(link.get('href'))[:17]))

    return movies

def find_actors(movie): 
    actors = []
    url = movie
    page = urllib2.urlopen(url)
    data = page.read()
    soup = BeautifulSoup(data)

    for link in soup.findAll('a', href = re.compile('http://m.imdb.com/name/nm')):
        actors.append(str(link.get('href'))[:33])

    return actors

graph = {}

def neighbors(actor):
    if actor in graph:
        return graph[actor]
    graph[actor] = []
    for movie in find_movies(actor):
        actors = find_actors(movie)
        for x in actors:
            if x not in graph[actor]:
                graph[actor].append(x)
    return graph[actor]

Bacon = "http://m.imdb.com/name/nm0000102/filmotype/actor?ref_=m_nmfm_1"

for x in neighbors(Bacon):
    print x
