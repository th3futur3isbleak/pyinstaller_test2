"""Console script for pyinstaller_test2."""

import sys
import click

@click.command()
def main(args=None):
    """Console script for pyinstaller_test2."""
    click.echo("Replace this message by putting your code into "
               "pyinstaller_test2.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
