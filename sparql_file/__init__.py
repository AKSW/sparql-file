from rdflib import ConjunctiveGraph
from rdflib_endpoint import SparqlEndpoint

DEFAULT_EXAMPLE_QUERY = "select * { ?s ?p ?o } limit 10"


def sparql_file(
    graph_file: str,
    example_query: str | None = None,
    graph_format: str | None = None,
):
    g = ConjunctiveGraph()

    if example_query is None:
        example_query = DEFAULT_EXAMPLE_QUERY

    with open(graph_file, "r") as graph_file_io:
        g.parse(source=graph_file_io, format=graph_format)

    # Return the SPARQL endpoint based on the RDFLib Graph
    return SparqlEndpoint(
        graph=g,
        example_query=example_query,
    )
