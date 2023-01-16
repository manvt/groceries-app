FILEPATH = "groceries.txt"


def get_todos(filepath=FILEPATH):
    """ Reads in the text document and returns
     the list of to-do items.
     """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("This will only print when you run the functions.py file")
    print(get_todos())