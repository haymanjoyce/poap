import click

import commands
from src.utils import file_handling


@click.command("hello")
def hello():
    click.echo("hello")


if __name__ == "__main__":
    hello()
