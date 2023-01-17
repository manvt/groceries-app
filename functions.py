UFILEPATH = "groceries.txt"
GFILEPATH = "gourmet.txt"


def get_usual(filepath=UFILEPATH):
    """ Reads in the text document and returns
     the list of to-do items.
     """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_usual(todos_arg, filepath=UFILEPATH):
    """ Write to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


def get_gourmet(filepath=GFILEPATH):
    """ Reads in the text document and returns
     the list of to-do items.
     """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_gourmet(todos_arg, filepath=GFILEPATH):
    """ Write to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)




if __name__ == "__main__":
    print("This will only print when you run the functions.py file")
    print(get_usual())