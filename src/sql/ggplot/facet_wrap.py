from jinja2 import Template
import math
import sql.connection
from sql.telemetry import telemetry


class facet:
    def __init__():
        pass

    def get_facet_values(self, table, column, with_):
        template = Template(
            """
            SELECT
            distinct ({{column}})
            FROM "{{table}}"
            """
        )
        query = template.render(table=table, column=column)

        conn = sql.connection.Connection.current

        values = conn.execute(query, with_).fetchall()
        n_plots = len(values)
        n_cols = len(values) if len(values) < 3 else 3
        n_rows = math.ceil(n_plots / n_cols)
        return values, n_rows, n_cols


class facet_wrap(facet):
    """
    Splits a plot into a matrix of panels

    Parameters
    ----------
    facet : str
        Column to groupby and plot on different panels.
    """

    @telemetry.log_call("facet-wrap-init")
    def __init__(self, facet: str, legend=True):
        self.facet = facet
        self.legend = legend

    def __add__(self, other):
        return other.__add__(other)
