import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    # session_state is a specific streamlit object, renders dict-like values
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("App for daily chores")
st.write("Increases organizational efficiency")


# the script is always executed for each user session
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun() # needed for checkboxes

st.text_input(label="", placeholder="Enter a new task",
              on_change=add_todo, key="new_todo")

