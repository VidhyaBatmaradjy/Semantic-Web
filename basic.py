import logging
import rdflib
from rdflib.graph import Graph, URIRef
from SPARQLWrapper import SPARQLWrapper, RDF
from rdflib.plugins.memory import IOMemory

# configuring logging
logging.basicConfig()
 
# configuring the end-point and constructing query
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
construct_query="""
      PREFIX bo: <http://www.semanticweb.org/vidhyabk/ontologies/2017/2/book.owl#>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>        
      PREFIX foaf: <http://xmlns.com/foaf/0.1/>
      PREFIX dbo: <http://dbpedia.org/ontology/>
      PREFIX dbp: <http://dbpedia.org/property/>
      
      CONSTRUCT {
      ?book rdf:type bo:Book .
      ?book bo:title ?name .
      ?book bo:written_by ?author .
      ?author rdf:type bo:Author .
      ?book bo:name ?authname .
      ?book bo:published_by ?publisher .
      ?publisher rdf:type bo:Publisher .
      ?book bo:illustrated_by ?illustrator .
      ?illustrator rdf:type bo:Illustrator .
      ?book bo:has_genre ?genre .
      ?genre rdf:type bo:Literary_Genre .
      ?book bo:has_language ?lang .
      ?lang rdf:type bo:Original_Language .
      ?book bo:isbn ?isbn .
      ?book bo:pages ?pages .
      
      ?book bo:has_version ?movie1 .
      ?movie1 rdf:type bo:Film_Version .
      ?movie1 bo:title ?filmname1 .
     
      
      }
       WHERE{
       ?book    rdf:type    dbo:Book ;
                 foaf:name   ?name ;
                 dbp:author  ?author .
        ?author  foaf:name   ?authname .
        OPTIONAL {?book dbo:literaryGenre ?genre .}
        OPTIONAL {?book dbo:language ?lang .}
        OPTIONAL {?book dbo:publisher ?publisher .}
        OPTIONAL {?book dbo:illustrator ?illustrator .}
        OPTIONAL {?book dbo:isbn ?isbn .}
        OPTIONAL {?book dbp:pages ?pages .}
        
        ?book   ^dbo:basedOn ?movie1 .
        ?movie1  rdf:type   dbo:Film ;
                foaf:name  ?filmname1
         FILTER ( str(?name) IN ("Three Comrades", "Strangers on a Train", "The Three Musketeers", "The Red Shoes", "Possession: A Romance", "Hostage", "Metropolis", "The Love of the Last Tycoon", "The Osterman Weekend", "There and Back Again", "Jaws", "The Keep") )
      }
       """
        
       
sparql.setQuery(construct_query)
sparql.setReturnFormat(RDF)

# creating the RDF store and graph
memory_store=IOMemory()
graph_id=URIRef("http://www.semanticweb.org/store/book")
g = Graph(store=memory_store, identifier=graph_id)
#rdflib.plugin.register('sparql', rdflib.query.Processor, 'rdfextras.sparql.processor', 'Processor')
#rdflib.plugin.register('sparql', rdflib.query.Result, 'rdfextras.sparql.query', 'SPARQLQueryResult')

# merging results and saving the store
g = sparql.query().convert()
g.parse("book.owl")
g.serialize("basic_example.owl", "xml")