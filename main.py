import click


@ click.group()
def main():
    pass


@main.command()
@click.argument('argument')
@click.option('--opt', '-o',
              envvar="NOTE")
def test(argument, opt):
    print(f'arg: {argument}, opt: {opt}')


@main.command()
def add():
    print("Add command executed")


if __name__ == '__main__':
    main()
