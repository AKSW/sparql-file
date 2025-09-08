import os

from . import sparql_file

GRAPH_FILE = os.getenv("GRAPH_FILE", "graph.ttl")
EXAMPLE_QUERY = os.getenv("EXAMPLE_QUERY")
GRAPH_FORMAT = os.getenv("GRAPH_FORMAT")

app = sparql_file(GRAPH_FILE, EXAMPLE_QUERY, GRAPH_FORMAT)
