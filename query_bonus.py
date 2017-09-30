import logging
import rdflib

#from _pyio import open

# configuring logging
logging.basicConfig()

query = """
PREFIX bo: <http://www.semanticweb.org/vidhyabk/ontologies/2017/2/book.owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>  
SELECT  ?name ?name1 ?imdb
WHERE { ?book rdf:type bo:Book .
        ?book bo:title ?name .
        ?book bo:name ?author .
        ?book bo:isbn ?isbn .
        ?book bo:has_version ?movie . 
        ?movie bo:title ?name1 .
        ?book bo:imdbPage ?imdb
    
      
        
      }"""

# creating the graph
g=rdflib.Graph()
result=g.parse("bonus_example.owl", "xml")
print("graph has %s statements.\n" % len(g))

# querying and displaying the results
print ('{0:20s} {1:15s} {2:10s}'.format("Book","Related Movie","IMDB Page"))
print('-------------------------------------------------------------')
for x,y,z in g.query(query):
    print ('{0:20s} {1:15s} {2:10s}'.format(x,y,z))
