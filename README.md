# SPARQL File

Serve an RDF file as an [RDFLib](https://rdflib.readthedocs.io/) Graph through a SPARQL endpoint served as [fastapi](https://fastapi.tiangolo.com/) with [rdflib-endpoint](https://pypi.org/project/rdflib-endpoint/) ([github](https://github.com/vemonet/rdflib-endpoint)).

## Run Locally

```
$ GRAPH_FILE=graph.ttl poetry run uvicorn sparql_file:app --host 0.0.0.0 --port 8080
```

## Run With Podman/Docker

```
$ task build
$ podman run -d --rm -v /path/to/graph_file.ttl:/data/graph.ttl:z -p 8080:8080 localhost/sparql_file:latest
```
