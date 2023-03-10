"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Models."""


if __name__ == "__main__":
    main(prog_name="models")  # pragma: no cover
