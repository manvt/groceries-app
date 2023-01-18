import streamlit as st

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


def add_grocery():
    grocery = st.session_state["new_grocery"] + "\n"
    groceries.append(grocery)
    functions.write_groceries(groceries)


def add_gourmet():
    gourmet = st.session_state["new_gourmet"] + "\n"
    gourmets.append(gourmet)
    functions.write_gourmets(gourmets)


groceries = get_groceries()
gourmets = get_gourmets()

st.title("Groceries App")
st.subheader(f"These are the groceries we need to buy")
st.write("This list is our usual suspects at the store..")
#reset = st.button("Reset", on_click=st.experimental_rerun())

for index, grocery in enumerate(groceries):
    checkbox_grocery = st.checkbox(grocery, key=grocery)
    if checkbox_grocery:
        #usuals.pop(index)
        write_groceries(groceries)
        del st.session_state[grocery]
        st.experimental_rerun()


st.text_input(label="New usual suspect items", placeholder="Add new usual suspect...",
              on_change=add_grocery, key='new_grocery')


st.write("This list is when we are feeling gourmet..")

for index, gourmet in enumerate(gourmets):
    checkbox_gourmet = st.checkbox(gourmet, key=gourmet)
    if checkbox_gourmet:
        gourmets.pop(index)
        write_gourmets(gourmets)
        del st.session_state[gourmet]
        st.experimental_rerun()



st.text_input(label="New gourmet items", placeholder="Add new gourmet items here...",
              on_change=add_gourmet, key='new_gourmet')

# st.session_state
