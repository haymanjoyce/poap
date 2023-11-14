# __main__.py

import click
from . import commands


@click.group()
@click.pass_context
def cli(context):
    pass


cli.add_command(commands.import_)
cli.add_command(commands.export)


cli()

