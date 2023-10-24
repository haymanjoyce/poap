# commands.py

import click


@click.command()
def hello():
    click.echo('hello')


@click.command()
def goodbye():
    click.echo('goodbye')


if __name__ == '__main__':
    hello()
