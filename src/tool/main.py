# __main__.py

import click
import commands


@click.group()
@click.pass_context
def cli(context):
    pass


cli.add_command(commands.import_)
cli.add_command(commands.export)


if __name__ == "__main__":
    cli()

