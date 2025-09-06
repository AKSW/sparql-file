from .utils import copy_file
from simpsons_rdf import simpsons
import os

from fastapi.testclient import TestClient


def test_endpoint_with_turtle_graph(tmp_path):
    p = tmp_path / "graph_file.ttl"
    copy_file(simpsons.graph_file, p)
    os.environ["GRAPH_FILE"] = str(p)

    from sparql_file.env import app

    client = TestClient(app)

    response = client.post(
        "/",
        data="select ?s ?p ?o {?s ?p ?o} limit 1",
        headers={"Content-Type": "application/sparql-query"},
    )
    assert response.status_code == 200
