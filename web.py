import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("Groceries App")
st.subheader(f"This is the groceries we need to buy")
st.write("This app will track our current grocery needs")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="New items", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')


# st.session_state
