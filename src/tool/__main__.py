import click


@click.command("hello")
def hello():
    click.echo("hello")


if __name__ == "__main__":
    hello()
