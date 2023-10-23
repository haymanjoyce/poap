# commands.py

import click

from typing import Any


@click.command()
def hello():
    click.echo('hello')


@click.command()
def goodbye() -> Any:
    click.echo('goodbye')


if __name__ == '__main__':
    hello()
