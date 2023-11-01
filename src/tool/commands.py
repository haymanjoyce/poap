# commands.py

import click


@click.command()
def hello():
    click.echo('hello')


@click.command()
def goodbye():
    click.echo('goodbye')


@click.command(name='export')
@click.option('--type', '-t', 'type_', default='xlsx', type=click.Choice(['xlsx', 'csv', 'pdf', 'png', 'pkl'], case_sensitive=False))
@click.option('--blank', '-b', is_flag=True, default=False, help="Gives you a blank template (xlsx only).")
@click.option('--sheet', '-s', 'sheet', type=click.STRING, default='all', help="Name a table (else exports all of them).")
def export(type_, blank, sheet):
    click.echo(blank)
    click.echo(type_)
    click.echo(sheet)


def open_():
    pass


if __name__ == '__main__':
    hello()
