import logging
import rdflib
from rdflib import Graph, URIRef
from SPARQLWrapper import SPARQLWrapper, RDF
from rdflib.plugins.memory import IOMemory


# configuring logging
logging.basicConfig()
 
# configuring the end-point and constructing query
# the given construct query will add the data from both DBPedia and LinkedMDB 

sparql = SPARQLWrapper("http://linkeddata.uriburner.com/sparql")
construct_query="""
      PREFIX bo: <http://www.semanticweb.org/vidhyabk/ontologies/2017/2/book.owl#>
      PREFIX  dbo:  <http://dbpedia.org/ontology/>
      PREFIX  dbp:  <http://dbpedia.org/property/>
      PREFIX  movie: <http://data.linkedmdb.org/resource/movie/>
      PREFIX  owl:  <http://www.w3.org/2002/07/owl#>
      PREFIX  rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX  rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      PREFIX  foaf: <http://xmlns.com/foaf/0.1/>
      PREFIX  dc:   <http://purl.org/dc/terms/>
      
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
      ?movie1 bo:release_date ?date .
    
      ?book bo:imdbPage ?imdbID .
     
      }
       WHERE
       { SERVICE <http://dbpedia.org/sparql>
      { ?book    rdf:type    dbo:Book ;
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
    SERVICE <http://data.linkedmdb.org/sparql>
      { ?filmname  foaf:page  ?imdbID ;
                  dc:title   ?filmname2 ;
                  dc:date   ?date
        FILTER regex(str(?imdbID), "www.imdb.com")
      }
    FILTER ( str(?filmname1) = str(?filmname2) )
  }"""

       
       
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

g.serialize("bonus_example.owl", "xml")
