todolist = []       
def create(tasks):
    todolist.append(tasks)
    print(f"Added: {tasks}")
def view(index = None):
    print(todolist)
    print(len(todolist))
    for i in range(0,len(todolist)):
        print(f"{i+1} - {todolist[i]}")
def remove(index = None):
    if index:
        todolist.remove(todolist[index])
        print(todolist)
        return 
    todolist.pop()
    print(todolist)
create("wake")
create("Travel")
create("eat")
view(index = 1)
remove(1)