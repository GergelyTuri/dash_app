import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from . import load_data, trace_ids

DATA = load_data.load_data()


def render(app: Dash) -> html.Div:
    @app.callback(
        Output(trace_ids.LINE_PLOT, "children"),
        [
            Input(trace_ids.TRACES_DROPDOWN, "value"),
        ],
    )
    def update_line_plot(selected_trace_types: list[str]) -> html.Div:
        # Handle case where no trace types are selected
        if not selected_trace_types:
            return html.Div("No data selected", id=trace_ids.LINE_PLOT)

        # Validate selected trace types against the columns in DATA
        valid_columns = [col for col in selected_trace_types if col in DATA.columns]

        # Handle case where no valid trace types match
        if not valid_columns:
            return html.Div("No matching trace types found", id=trace_ids.LINE_PLOT)

        # Create the line plot
        fig = px.line(
            DATA,
            y=valid_columns,
            labels={"value": "Trace Values", "variable": "Trace Types"},
        )

        return html.Div(dcc.Graph(figure=fig), id=trace_ids.LINE_PLOT)

    return html.Div(id=trace_ids.LINE_PLOT)
