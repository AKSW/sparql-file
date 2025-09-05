import typer
import uvicorn

from . import DEFAULT_EXAMPLE_QUERY, sparql_file

app = typer.Typer()


@app.command()
def cli(
    graph_file: str,
    host: str = "localhost",
    port: int = 8000,
    example_query: str = DEFAULT_EXAMPLE_QUERY,
    graph_format: str | None = None,
):
    """Start a SPARQL 1.1 endpoint based on the given RDF file.

    If you want to bind to every address on the IPv4 and IPv6 stack set --host ''
    (cf. https://chaos.social/@white_gecko/114184354432052312)
    """
    endpoint = sparql_file(graph_file, example_query, graph_format)
    uvicorn.run(endpoint, host=host, port=port)


if __name__ == "__main__":
    app()
