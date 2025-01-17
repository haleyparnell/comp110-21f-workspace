"""Utility functions."""

__author__ = "730514769"

# Define your functions below
from csv import DictReader


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
    for column in column_table:
        test: list[str] = []
        i: int = 0
        if n >= len(column_table):
            return column_table
        else:
            while i < n:
                test.append(column_table[column][i])
                i += 1
            result[column] = test
    return result


def select(column: dict[str, list[str]], name: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based 'table' with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    i: int = 0
    test: list[str] = []
    for each_column in name:
        result[each_column] = name
        while i < len(column):
            test.append(column[each_column][i])
            i += 1
            result[each_column] = test

    return result


def concat(dict_one: dict[str, list[str]], dict_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based 'table' with two-columns based tables combined."""
    result: dict[str, list[str]] = {}
    return result