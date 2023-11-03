# commands.py

import click


@click.command()
def hello():
    click.echo('hello')


@click.command()
def goodbye():
    click.echo('goodbye')


@click.command(name='export')
@click.option('--name', '-n', 'name', type=click.STRING, show_default=True, help="The file name.")
@click.option('--type', '-t', 'type_', default='xlsx', type=click.Choice(['xlsx', 'csv', 'pdf', 'png', 'pkl'], case_sensitive=False), help="The file type.")
@click.option('--location', '-l', 'location', type=click.STRING, show_default=True, help="Where you want to export the file to.")
@click.option('--blank', '-b', is_flag=True, default=False, help="Gives you a blank template (xlsx only).")
@click.option('--sheet', '-s', 'sheet', type=click.STRING, default='all', help="Name a table (else exports all of them).")
def export(type_, blank, sheet, location, name):
    click.echo(blank)
    click.echo(type_)
    click.echo(sheet)
    click.echo(location)
    click.echo(name)


def open_():
    pass


if __name__ == '__main__':
    hello()
