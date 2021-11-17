"""Utility functions."""

__author__ = "730514769"

# Define your functions below
from csv import DictReader

from tabulate import tabulate


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
        
    return result


def head(column_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based 'table' with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    i: int = 0
    
    # TODO
    return result


def select(column: dict[str, list[str]], name: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based 'table' with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    # TODO
    return result


def concat(dict_one: dict[str, list[str]], dict_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based 'table' with two-columns based tables combined."""
    result: dict[str, list[str]] = {}
    # TODO
    return result