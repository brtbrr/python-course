import sys
import click

@click.command()
@click.argument("filepath", type=click.Path(), default="")
def task1(filepath):
    num = 0

    if not filepath:
        for line in sys.stdin:
            num += 1
            click.echo(f'    {num:2}  {line.strip()}')
    else:
        try:
            with open(filepath, 'r') as f:
                for line in f:
                    num += 1
                    click.echo(f'    {num:2}  {line.strip()}')
        except IOError:
            sys.exit(f'open: No such file or directory: \'{filepath}\'')

task1()
