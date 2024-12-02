from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout
from src.data import load_data

DATA_LOCATION = (
    "E:/test/42_1-241030-092508/analysis/fiber_data_20241030_092533_32_623.csv"
)


def main() -> None:
    data = load_data.load_data(DATA_LOCATION)
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Traces"
    app.layout = create_layout(app, data)
    app.run_server(debug=True)


if __name__ == "__main__":
    main()
