from rdflib import Graph
from rdflib_endpoint import SparqlEndpoint
from textwrap import dedent

import os

GRAPH_FILE = os.getenv("GRAPH_FILE")
EXAMPLE_QUERY = os.getenv("EXAMPLE_QUERY", dedent("""
select * { ?s ?p ?o } limit 10
""").strip())

g = Graph()

with open(GRAPH_FILE, "r") as graph_file_io:
    g.parse(source=graph_file_io)

# Start the SPARQL endpoint based on the RDFLib Graph
app = SparqlEndpoint(
    graph=g,
    example_query=EXAMPLE_QUERY,
)
