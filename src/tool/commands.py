import click
from datetime import datetime
from pathlib import Path
from src.tool.export import blank_

HOME = str(Path.home())


@click.command(name='import')
@click.option('--check', '-c', default=True, help="Checks document content before import.")
def import_(check):
    click.echo(check)


@click.command(name='export')
@click.option('--name', '-n', 'name', type=click.STRING, default=f"export_{datetime.now().strftime("%Y%m%d_%H%M%S")}", show_default=True)
@click.option('--type', '-t', 'type_', default='xlsx', show_default=False, type=click.Choice(['xlsx', 'csv', 'json', 'svg', 'pdf', 'png', 'pkl'], case_sensitive=False))
@click.option('--location', '-l', 'location', type=click.STRING, default=HOME, show_default=True)
@click.option('--blank', '-b', is_flag=True, default=False, help="Gives you a blank template (xlsx only).")
@click.option('--sheet', '-s', 'sheet', type=click.STRING, default='all', show_default=True)
@click.option('--meta', '-m', 'meta', type=click.Choice(['none', 'some', 'all'], case_sensitive=False), default='none', show_default=True, help="Meta-data options.")
def export(type_, blank, sheet, location, name, meta):
    click.echo(blank)
    click.echo(type_)
    click.echo(sheet)
    click.echo(location)
    click.echo(name)
    click.echo(meta)
    if blank:
        blank_()


@click.command(name="list")
# list folders with sort and filter options
def list_():
    pass


@click.command(name="open")
# open in read or write mode (svgs, json, csv)
def open_():
    pass


@click.command(name="close")
# close a file with options to save and save as
def close():
    pass


@click.command(name="run")
# run a script for example
def run():
    pass

