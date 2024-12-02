from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from . import trace_ids


def render(app: Dash) -> html.Div:
    trace_types = ["raw_405nm", "raw_465nm", "dff"]

    @app.callback(
        Output(trace_ids.TRACES_DROPDOWN, "value"),
        Input(trace_ids.SELECT_ALL_TRACES_BUTTON, "n_clicks"),
    )
    def select_all_traces(_: int) -> list[str]:
        return trace_types

    return html.Div(
        children=[
            html.H6("Select a trace type"),
            dcc.Dropdown(
                id=trace_ids.TRACES_DROPDOWN,
                options=[
                    {"label": trace_type, "value": trace_type}
                    for trace_type in trace_types
                ],
                value=trace_types,
                multi=True,
            ),
            html.Button(
                className="dropdown-button",
                children=["Select all"],
                id=trace_ids.SELECT_ALL_TRACES_BUTTON,
                n_clicks=0,
            ),
        ]
    )
