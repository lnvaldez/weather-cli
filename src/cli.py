import typer
from src.commands.weather_commands import location, coordinate
from src.commands.util_commands import clear

app = typer.Typer()


app.command()(location)
app.command(context_settings={"ignore_unknown_options": True})(coordinate)
app.command()(clear)


if __name__ == "__main__":
    app()
