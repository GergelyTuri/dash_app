from dash import Dash, html

from . import line_plots, traces_dropdown


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container", children=[traces_dropdown.render(app)]
            ),
            line_plots.render(app),
        ],
    )
