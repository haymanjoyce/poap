import click

from src.poap.export import ExportManager


@click.command(name='import')
@click.option('--check', '-c', default=True, help="Checks document content before import.")
def import_(check):
    click.echo(check)


@click.command(name='export')
@click.option('--name', '-n', 'file_name', type=click.STRING)
@click.option('--type', '-t', 'file_type', default='xlsx', show_default=False, type=click.Choice(['xlsx', 'csv', 'json', 'svg', 'pdf', 'png', 'pkl'], case_sensitive=False))
@click.option('--location', '-l', 'location', type=click.STRING)
@click.option('--blank', '-b', is_flag=True, default=False, help="Gives you a blank template (xlsx only).")
@click.option('--sheet', '-s', 'sheet_name', type=click.STRING, default='0', show_default=True)
@click.option('--meta', '-m', 'meta', type=click.Choice(['none', 'some', 'all'], case_sensitive=False), default='none', show_default=True, help="Meta-data options.")
def export(file_name, file_type, location, blank, sheet_name, meta):
    export_manager = ExportManager(file_name, file_type, location, blank, sheet_name, meta)
    print(export_manager.__dict__)


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

