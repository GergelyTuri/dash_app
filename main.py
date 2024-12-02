from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout


def main() -> None:
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Traces"
    app.layout = create_layout(app)
    app.run_server(debug=True)


if __name__ == "__main__":
    main()
