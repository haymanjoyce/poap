# commands.py

import click


@click.command()
def hello():
    click.echo("hello")
    print("hello worked")


print("loaded")
