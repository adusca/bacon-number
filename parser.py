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
        movies.append("http://m.imdb.com" + str(link.get('href')))

    return movies

def find_actors(movie): 
    actors = []
    url = movie
    page = urllib2.urlopen(url)
    data = page.read()
    soup = BeautifulSoup(data)

    for link in soup.findAll('a', href = re.compile('/name/nm')):
        actors.append(link.get('href'))

    return actors

graph = {}

def neighbors(actor):
    graph[actor] = []
    for movie in find_movies(actor):
        actors = find_actors(movie)
        for x in actors:
            if x not in graph[actor]:
                graph[actor].append(x)
    return graph[actor]

Bacon = "http://m.imdb.com/name/nm0000102/filmotype/actor?ref_=m_nmfm_1"
#print find_movies(Bacon)
#for x in find_actors("http://m.imdb.com/title/tt1951265/"):
#    print x
print neighbors(Bacon)
