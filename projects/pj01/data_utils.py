"""Utility functions."""

__author__ = "730482431"

# Some helpful utility functions for working with csv files

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


def head(dish: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Allows the user to see the first few columns of data."""
    soap: dict[str, list[str]] = {}
    for columns in dish:
        kagebunshin: list[str] = []
        i: int = 0
        if n > len(dish[columns]):
            n = len(dish[columns])
        while i < n:
            kagebunshin.append(dish[columns][i])
            i += 1
        soap[columns] = kagebunshin
    return soap


def select(gokkaku: dict[str, list[str]], katsu: list[str]) -> dict[str, list[str]]:
    """Allows the user to select which columns/data they want to access."""
    chidori: dict[str, list[str]] = {}
    for column in katsu:
        chidori[column] = gokkaku[column]
    return chidori


def concat(dish: dict[str, list[str]], soap: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces two dicts from one."""
    book: dict[str, list[str]] = {}
    for column in dish:
        book[column] = dish[column]
    for column in soap:
        if column in book:
            i: int = 0
            while i < len(soap[column]):
                book[column].append(soap[column][i])
                i += 1
        else:
            book[column] = soap[column]
    return book


def concat_int(dish: dict[str, int], soap: dict[str, int]) -> dict[str, int]:
    """Produces two dicts from one, typically from count."""
    book: dict[str, int] = {}
    for column in dish:
        book[column] = dish[column]
    for column in soap:
        book[column] = soap[column]
    return book


def count(notes: list[str]) -> dict[str, int]:
    """Produces a dict with a count of its keys/values."""
    book: dict[str, int] = {}
    for element in notes:
        if element not in book:
            book[element] = 1
        else:
            if element in book:
                book[element] += 1
    return book


def addem_up(x: dict[str, int]) -> int:
    """Adds all the values from the count function."""
    lst_nums: list[int] = []
    for key in x:
        lst_nums.append(x[key])
    i: int = 0
    total: int = 0
    while i < len(lst_nums):
        total += lst_nums[i]
        i += 1
    return total


def git_listy(column_reader: dict[str, list[str]], response: str) -> dict[str, list[str]]:
    """Given a dictionary, this function returns all wanted key value pairs."""
    mt_list: list[str] = []
    mt_list_zwei: list[str] = []
    mt_dict: dict[str, list[str]] = {}
    column: list[str] = []
    for key in column_reader:
        column.append(key)
    i: int = 0
    for element in column_reader:
        while i < len(column_reader[element]):
            mt_list.append(column_reader[element][i])
            i += 1
    for element in mt_list:
        if element == response:
            mt_list_zwei.append(element)
    for element in column:
        mt_dict[element] = mt_list_zwei
    return mt_dict


def eq(x: dict[str, list[str]]) -> dict[str, list[str]]:
    """Makes all the values of all keys equivalent in length. Only works for two columns in a dict."""
    mt_list = []
    for key in x:
        mt_list.append(key)
    if len(x[mt_list[0]]) < len(x[mt_list[1]]):
        num: int = len(x[mt_list[1]]) - len(x[mt_list[0]])
        i: int = 0
        while i < num:
            x[mt_list[1]].pop(len(x[mt_list[1]]) - 1)
            i += 1
    elif len(x[mt_list[0]]) > len(x[mt_list[1]]):
        num: int = len(x[mt_list[0]]) - len(x[mt_list[1]])
        i: int = 0
        while i < num:
            x[mt_list[0]].pop(len(x[mt_list[0]]) - 1)
            i += 1
    else: 
        pass
    return x


def ratings_filter(data_reader: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Reads through a column and filters out values less than or equal to n."""
    mt_list: list[str] = []
    mt_list_zwei: list[int] = []
    mt_list_drei: list[str] = []
    mt_dict: dict[str, list[str]] = {}
    i: int = 0
    for element in data_reader:
        while i < len(data_reader[element]):
            mt_list.append(data_reader[element][i])
            i += 1
    for str_elem in mt_list:
        mt_list_zwei.append(int(str_elem))
    i = 0
    filtered = filter(lambda num: num > n, mt_list_zwei)
    filtered_list = list(filtered)
    for int_elm in filtered_list:
        mt_list_drei.append(str(int_elm))
    for element in data_reader:
        mt_dict[element] = mt_list_drei
    return mt_dict