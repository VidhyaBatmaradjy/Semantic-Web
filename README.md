# Semantic-Web
Master's mini project: Ontology Construction for book search

Ontology Definition:
An ontology has been developed for searching novels and finding movies that were taken based on the corresponding novel if any. i.e. users in addition to finding novel details, can also find the movies based on novels and get more information using the corresponding IMDB review page if they are interested in watching that movie.

Ontology Construction
Features:
Basic: The user can query the ontology to find the basic details of any novel namely
• Book Name
• Author
• Publisher
• Illustrator
• ISBN
• No. of pages
• Genre
• Movie name (if any)
  
Bonus: This query to the local ontology answers a question that cannot be answered by either remote knowledge base alone. i.e. the user can query for movies based on novels (DBPedia) and get the following details(LinkedMDB).
• Movie release date
• IMDB review link for the movie.

1. Onto Graph
a) Generic view

![alt text](https://github.com/VidhyaBatmaradjy/Semantic-Web/blob/master/screenshots/onto_graph1.png)


2. Classes

![alt text](https://github.com/VidhyaBatmaradjy/Semantic-Web/blob/master/screenshots/classes.png)


3. Object Properties

![alt text](https://github.com/VidhyaBatmaradjy/Semantic-Web/blob/master/screenshots/object_properties.png)


4. Data Properties

![alt text](https://github.com/VidhyaBatmaradjy/Semantic-Web/blob/master/screenshots/data_properties.png)


SECTION 2
Challenges Faced
The challenges faced during the construction of ontology are as follows
1. Unclear boundaries of definitions for a few entities.
2. Difficulty in striking the right balance between the light, structured, local ontology and data from external  
   repositories which increases the chance of expressing data fragments but lowers accuracy among annotators.
3. Missing data fragments.
4. Many public endpoints have been closed or do not contain updated
information.
5. Issues fusing information as there is no unique name assumption which is common in other representative systems.

Solutions
Given below are some of the solutions.
1. Use of SPARQL Optional increased expressivity and made it easier to model complex data and populate more triples due to its ability to deal with sparsity in data.
2. Use of SERVICE keyword enabled to query a set of SPARQL endpoints using a single federated query. For example, the bonus query queries both DBPedia and LinkedMDB endpoints. DBPedia is asked for all the properties (author, publisher, ISBN, etc.) of a novel including the movie name based on that novel should they exist. Then the results are joined with the results of LinkedMDB, which asks for the release date and IMDB link for the movie name obtained from DBPedia.
  
SECTION 3
External Semantic Repository used
1. Basic: DBPEDIA
2. Bonus: DBPEDIA + LINKEDMDB

Endpoints used
1. http://dbpedia.org/sparql (used to get basic properties of novel including movie name if any)
2. http://data.linkedmdb.org/sparql (used to get the corresponding release date & IMDB link for the DBPedia movie name if any)
3. http://linkeddata.uriburner.com/sparql (used in bonus.py for linking data from DBPedia & LinkedMDB)

SECTION 4

Source code files
1. A Protégé-OWL ontology (book.owl).
2. A python script to populate the basic ontology (basic.py).
3. A python script to query the local store to demonstrate to the user that information can be 
   easily accessed (query_basic.py).
4. A python script to populate the bonus data to ontology (bonus.py)
5. A python script for bonus query (query_bonus.py)
   
Output OWL files

The following output OWL files will be generated by running the following python script.
1. basic.py => basic_example.owl 2. bonus.py => bonus_example.owl

Steps for code execution

Step 1: Open book.owl to check the construction of local ontology. This OWL does not contain any instances.

(Basic Part)
Step 2: Run basic.py. The script generates a new OWL by name basic_example.owl. It queries only DBPedia and populates the local ontology with instances from DBPedia. The instances can be checked by opening the generated OWL. The data properties namely “imdbPage” and “release_date” will not have any values. The values will be populated in the bonus part.

Step 3: Next, run query_basic.py to query the local ontology (basic_example.owl) generated from step 2. This script retrieves all novels which has author, ISBN and related movie. In this case, we have only 3 books that satisfies the condition out of the 12 novels populated.

(Bonus Part)
Step 4: Run bonus.py. The script generates a new OWL by name bonus_example.owl. This script executes a federated query, joins and populates results from both DBPedia and LinkedMDB. The instances can be checked by opening the generated OWL. The data properties namely “imdbPage” and “release_date” will now have values for corresponding movies. This script execution will take a few more seconds (about 1 minute) than the basic part as multiple endpoints are queried.

Step 5: Next, run query_bonus.py to query the local ontology (bonus_example.owl) generated from step 4. The script retrieves the IMDB link for all the movies displayed when executing query_basic.py. In this case, the movies related to the same 3 books that were displayed in the above screenshot from step 3.

 PS: The above steps will dynamically generate the 2 OWL output files. But as the public endpoints sometimes go down for maintenance, the 2 OWL files (basic_example.owl, bonus_example.owl) required by the scripts for querying have been placed in a folder “backup” for ease. Please move it to the root folder and then run (query_basic.py, query_bonus.py) only if required or you encounter any errors.
