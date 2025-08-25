from rdflib import Graph
from rdflib_endpoint import SparqlEndpoint

DEFAULT_EXAMPLE_QUERY = "select * { ?s ?p ?o } limit 10"


def sparql_file(
    graph_file: str,
    example_query: str = DEFAULT_EXAMPLE_QUERY,
    graph_format: str | None = None,
):
    g = Graph()

    with open(graph_file, "r") as graph_file_io:
        g.parse(source=graph_file_io, format=None)

    # Return the SPARQL endpoint based on the RDFLib Graph
    return SparqlEndpoint(
        graph=g,
        example_query=example_query,
    )
