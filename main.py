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


if __name__ == '__main__':
    main()
