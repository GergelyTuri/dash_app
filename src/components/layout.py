import pandas as pd
from dash import Dash, html

from . import line_plots, traces_dropdown


def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[traces_dropdown.render(app, data)],
            ),
            line_plots.render(app, data),
        ],
    )
