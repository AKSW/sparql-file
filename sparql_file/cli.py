import typer
import uvicorn

from . import DEFAULT_EXAMPLE_QUERY, sparql_file

app = typer.Typer()


@app.command()
def cli(
    graph_file: str,
    host: str = "0.0.0.0",
    port: str = "8000",
    example_query: str = DEFAULT_EXAMPLE_QUERY,
    graph_format: str | None = None,
):
    """Start a SPARQL 1.1 endpoint based on the given RDF file."""
    endpoint = sparql_file(graph_file, example_query)
    uvicorn.run(endpoint, host=host, port=port)


if __name__ == "__main__":
    app()
