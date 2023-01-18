GROCERIES_FILEPATH = "groceries.txt"
GOURMET_FILEPATH = "gourmet.txt"


def get_groceries(filepath=GROCERIES_FILEPATH):
    """ Reads in the text document and returns
     the list of to-do items.
     """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_groceries(todos_arg, filepath=GROCERIES_FILEPATH):
    """ Write to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


def get_gourmets(filepath=GOURMET_FILEPATH):
    """ Reads in the text document and returns
     the list of to-do items.
     """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_gourmets(todos_arg, filepath=GOURMET_FILEPATH):
    """ Write to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)




if __name__ == "__main__":
    print("This will only print when you run the functions.py file")
    print(get_groceries())
    print(get_gourmets())