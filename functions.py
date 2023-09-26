def get_todos(filepath="todos.txt"):
    """ read the text file and return the list
    of todo items """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local

def write_todos(todos_arg,filepath="todos.txt"):
    """ Write the todo items list int the text file """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

if __name__ == "__main__":
    print("hello yaeh")


