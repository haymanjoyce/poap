import click
from src.utils import filing


@ click.group()
@ click.option('--shared', '-s', type=str)
@ click.pass_context
def main(meta, shared):
    # print(type(meta))
    # print(dir(meta))
    meta.obj = shared
    if meta.obj is None:
        meta.obj = 'No shared value'
    # print(f'{meta.obj}')


@main.command()
@click.argument('argument')
@click.option('--opt', '-o', envvar="NOTE", type=str)
@click.pass_context
def test(meta, argument, opt):
    if opt is None:
        opt = 'No option'
    print(f'arg: {argument}, opt: {opt}, meta: {meta.obj}')
    # print(os.environ)


@main.command()
def add():
    print("Add command executed")
    prompt = click.prompt("Please enter prompt:", default="Default prompt")
    print(prompt)


@main.command()
def load():
    file_name = '../../samples/sample.csv'
    filing.read_file_csv(file_name)


@main.command()
@click.argument('table')
def export():
    pass

