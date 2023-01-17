import streamlit as st
import functions


usuals = functions.get_usual()
gourmets = functions.get_gourmet()


def add_usual():
    usual = st.session_state["new_usual"] + "\n"
    usuals.append(usual)
    functions.write_usual(usuals)


def add_gourmet():
    gourmet = st.session_state["new_gourmet"] + "\n"
    gourmets.append(gourmet)
    functions.write_gourmet(gourmets)


st.title("Groceries App")
st.subheader(f"These are the groceries we need to buy")
st.write("This list is our usual suspects at the store..")
#reset = st.button("Reset", on_click=st.experimental_rerun())

for index, usual in enumerate(usuals):
    checkbox = st.checkbox(usual, key=usual)
    if checkbox:
        #usuals.pop(index)
        functions.write_usual(usuals)
        del st.session_state[usual]
        st.experimental_rerun()


st.text_input(label="New usual suspect items", placeholder="Add new usual suspect...",
              on_change=add_usual, key='new_usual')


st.write("This list is when we are feeling gourmet..")

for index, gourmet in enumerate(gourmets):
    checkbox = st.checkbox(gourmet, key=gourmet)
    if checkbox:
        gourmets.pop(index)
        functions.write_gourmet(gourmets)
        del st.session_state[gourmet]
        st.experimental_rerun()



st.text_input(label="New gourmet items", placeholder="Add new gourmet items here...",
              on_change=add_gourmet, key='new_gourmet')

# st.session_state
