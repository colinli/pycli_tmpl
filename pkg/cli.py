import click
from pkg.module import mod_a, mod_b

@click.group()
def cli():
    pass

@click.command(help="mod a")
def moda():
    mod_a()

@click.command(help="mob d")
def modb():
    mod_b()

cli.add_command(moda)
cli.add_command(modb)

if __name__ == '__main__':
    cli()
