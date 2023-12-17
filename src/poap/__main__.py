import click
from src.poap import commands



@click.group()
def cli():
    pass


cli.add_command(commands.import_)
cli.add_command(commands.export)


if __name__ == "__main__":
    cli()

