"""Command-line interface for {{ cookiecutter.project_name }}."""

import argparse
import sys

import numpy as np

from . import __version__


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser."""
    parser = argparse.ArgumentParser(
        prog="{{ cookiecutter.project_slug }}",
        description="{{ cookiecutter.description }}",
    )
    parser.add_argument(
        "-V", "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args(argv)

    if args.verbose:
        print("Verbose mode enabled")

    print("Hello from {{ cookiecutter.project_name }}!")

    data = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    print(f"Array: {data}")
    print(f"Mean:  {np.mean(data):.2f}")
    print(f"Sum:   {np.sum(data):.2f}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
