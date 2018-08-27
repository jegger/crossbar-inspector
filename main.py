#!venv/bin/python

import click
from cli.registration import reg
from cli.subscription import sub

@click.group()
def cli():
    """A tool which lets you modify users, licenses etc.
    User COMMAND --help for more.
    """
    pass


cli.add_command(reg)
cli.add_command(sub)

if __name__ == '__main__':
    cli()
