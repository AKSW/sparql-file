from rdflib import Dataset
from rdflib_endpoint import SparqlEndpoint

DEFAULT_EXAMPLE_QUERY = "select * { ?s ?p ?o } limit 10"


def sparql_file(
    graph_file: str,
    example_query: str | None = None,
    graph_format: str | None = None,
):
    ds = Dataset()

    if example_query is None:
        example_query = DEFAULT_EXAMPLE_QUERY

    with open(graph_file, "r") as graph_file_io:
        ds.parse(source=graph_file_io, format=graph_format)

    # Return the SPARQL endpoint based on the RDFLib Graph
    return SparqlEndpoint(
        graph=ds,
        example_query=example_query,
    )
