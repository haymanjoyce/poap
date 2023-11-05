# commands.py

import click
from . import HOME
from datetime import datetime


@click.command()
def import_():
    pass


@click.command(name='export')
@click.option('--name', '-n', 'name', type=click.STRING, default=f"export_{datetime.now().strftime("%Y%m%d_%H%M%S")}", show_default=True)
@click.option('--type', '-t', 'type_', default='xlsx', show_default=False, type=click.Choice(['xlsx', 'csv', 'pdf', 'png', 'pkl'], case_sensitive=False))
@click.option('--location', '-l', 'location', type=click.STRING, default=HOME, show_default=True)
@click.option('--blank', '-b', is_flag=True, default=False, help="Gives you a blank template (xlsx only).")
@click.option('--sheet', '-s', 'sheet', type=click.STRING, default='all', show_default=True)
def export(type_, blank, sheet, location, name):
    click.echo(blank)
    click.echo(type_)
    click.echo(sheet)
    click.echo(location)
    click.echo(name)


def open_():
    pass


def close():
    pass

