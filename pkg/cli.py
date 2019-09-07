import click
from pkg.module import moda, modb

@click.group()
def cli():
    pass

@click.command(help="mod a")
def _moda():
    moda()

@click.command(help="mob d")
def _modb():
    modb()

cli.add_command(_moda)
cli.add_command(_modb)

if __name__ == '__main__':
    cli()
