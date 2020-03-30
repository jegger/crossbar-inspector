#!venv/bin/python

import click
from cli.registration import reg
from cli.subscription import sub
from cli.publish import publish
from cli.sessions import sessions

@click.group()
def cli():
    """A tool which lets you modify users, licenses etc.
    User COMMAND --help for more.
    """
    pass


cli.add_command(reg)
cli.add_command(sub)
cli.add_command(publish)
cli.add_command(sessions)

if __name__ == '__main__':
    cli()
