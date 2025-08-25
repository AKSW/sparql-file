import os

from . import sparql_file

GRAPH_FILE = os.getenv("GRAPH_FILE")
EXAMPLE_QUERY = os.getenv(
    "EXAMPLE_QUERY",
)

app = sparql_file(GRAPH_FILE, EXAMPLE_QUERY)
