def create(task):
    file = open("Todolist.txt", "a")
    file.write(task + "\n")
    file.close()
def view():
    try:
        file = open("Todolist.txt", "r")   
        content = file.read()
        if not content:
            print("Not found")
        print(content)
        file.close   
    except Exception as e:
        print(str(e))
def delete(index = None):  
    file = open("Todolist.txt", "r")
    lines = file.readlines()
    
    if 0 < index <= len(lines):
        del lines[index-1] 
    
    writefile = open("Todolist.txt",'w')
    writefile.writelines(lines)
    file.close()        
    writefile.close()
    print("line removed")
while True:
    print("To do list Menu")
    print("1. Add:")
    print("2. View")
    print("3. Delete")
    print("4. Exit")
    value = int(input("Choose the number between (1 to 4)? "))
    match value:
        case 1:
            task = input("Create Task: \n")
            create(task)
        case 2:
            view() 
        case 3:
            index = int(input("Enter line number you want to remove? \n"))
            delete(index = index )
        case 4:
            exit()    
              
        
