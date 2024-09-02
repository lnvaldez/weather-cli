import typer
from src.commands.weather_commands import location, coordinate

app = typer.Typer()


app.command()(location)
app.command()(coordinate)


if __name__ == "__main__":
    app()
