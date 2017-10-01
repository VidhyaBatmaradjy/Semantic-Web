import logging
import rdflib

# configuring logging
logging.basicConfig()

query = """
PREFIX bo: <http://www.semanticweb.org/vidhyabk/ontologies/2017/2/book.owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>  
SELECT  ?name ?author ?isbn ?name1
WHERE { ?book rdf:type bo:Book .
        ?book bo:title ?name .
        ?book bo:name ?author .
        ?book bo:isbn ?isbn .
        ?book bo:has_version ?movie . 
        ?movie bo:title ?name1 .
        
       
      
        
      }"""

# creating the graph
g=rdflib.Graph()
result=g.parse("basic_example.owl", "xml")
print("graph has %s statements.\n" % len(g))

# querying and displaying the results
print ('{0:21s} {1:14s} {2:16s} {3:10s}'.format("Book","Author","ISBN","Related Movie"))
print('--------------------------------------------------------------------------')
for x,y,z,s in g.query(query):
    print ('{0:21s} {1:14s} {2:16s} {3:10s}'.format(x,y,z,s))
