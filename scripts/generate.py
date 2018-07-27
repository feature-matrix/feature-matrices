import os
import glob
from jinja2 import Template
import pandas as pd

template = Template(
    open(os.path.join(os.path.dirname(__file__), "template.html")).read())


def render(matrix_path):
    name = os.path.splitext(os.path.basename(matrix_path))[0]

    matrix = pd.read_table(matrix_path).set_index(
        ["feature", "software"], drop=False)

    path = os.path.join("src", name + ".html")
    os.makedirs("src", exist_ok=True)
    with open(path, "w") as out:
        out.write(
            template.render(name=name, matrix=matrix, matrix_path=matrix_path))


for matrix in glob.glob("data/*.tsv"):
    render(matrix)
