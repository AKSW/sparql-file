from rdflib import Graph
from rdflib_endpoint import SparqlEndpoint
import os

GRAPH_FILE = os.getenv("GRAPH_FILE")

g = Graph()

with open(GRAPH_FILE, "r") as graph_file_io:
    g.parse(source=graph_file_io)

# Start the SPARQL endpoint based on the RDFLib Graph
app = SparqlEndpoint(
    graph=g,
)
