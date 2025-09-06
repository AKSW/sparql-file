from sparql_file import sparql_file
from .utils import copy_file
from simpsons_rdf import simpsons


def test_api_with_turtle_graph(tmp_path):
    p = tmp_path / "graph_file.ttl"
    copy_file(simpsons.graph_file, p)
    sparql_file(p)


def test_api_with_turtle_graph_specify_format(tmp_path):
    p = tmp_path / "graph_file.ttl"
    copy_file(simpsons.graph_file, p)
    sparql_file(p, graph_format="turtle")
