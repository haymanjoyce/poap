# commands.py

import click


@click.command()
def hello():
    click.echo('hello')


@click.command()
def goodbye():
    click.echo('goodbye')


@click.command()
@click.option('--type', '-t', 'type_', default='excel', type=click.STRING, help="Accepted file types are 'excel', 'pdf', or 'png'.")
@click.option('--blank', '-b', is_flag=True, default=False)
def export(type_, blank):
    click.echo(blank)
    click.echo(type_)


if __name__ == '__main__':
    hello()
