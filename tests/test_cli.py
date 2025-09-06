from sparql_file.cli import app
from .utils import copy_file
from simpsons_rdf import simpsons
import pytest

from typer.testing import CliRunner

runner = CliRunner()


@pytest.mark.skip(reason="I don't know how to send send sig term in this case")
def test_cli_with_turtle_graph(tmp_path):
    p = tmp_path / "graph_file.ttl"
    copy_file(simpsons.graph_file, p)

    result = runner.invoke(app, [f"{p}"])
    assert result.exit_code == 0


@pytest.mark.skip(reason="I don't know how to send send sig term in this case")
def test_cli_with_turtle_graph_specify_format(tmp_path):
    p = tmp_path / "graph_file.ttl"
    copy_file(simpsons.graph_file, p)

    result = runner.invoke(app, [f"{p}", "--graph-format", "turtle"])
    assert result.exit_code == 0
