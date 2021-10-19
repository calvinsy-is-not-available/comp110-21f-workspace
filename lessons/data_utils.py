"""Some helpful utility functions for working with csv files"""

from csv import DictReader


# reading the lines of a csv file
def read_csv_rows(file_name: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    # Open a handle to the data file
    file_handle = open(file_name, "r", encoding="utf8")
    # Prepare to read the data file as a csv rather than just strings
    csv_reader = DictReader(file_handle)
    # Read each row of the csv line by line.
    for row in csv_reader:
        result.append(row)
    # Close that file to free up resources that it was using.
    file_handle.close()
   
    return result 


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Reads the rows of a csv into a column based thing."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Morph a row-oriented table to a column-oriented (or representation) of a table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result