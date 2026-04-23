"""Tests for the CLI module."""

from {{ cookiecutter.module_name }}.cli import main


def test_main_succeeds():
    assert main([]) == 0
