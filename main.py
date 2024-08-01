todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.lower().strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
             for index, item in enumerate(todos):
                 item = item.title()
                 print(f"{index + 1}-{item}")
        case "edit":
            number = int(input("Enter the number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo
        case "exit":
            break
        case _:
            print("Hey, you entered an unknow command")
print("Bye!!")




