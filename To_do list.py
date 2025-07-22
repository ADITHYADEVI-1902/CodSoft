tasks = []
while True:
    print("Todo List App\n1. Add task \n2. Show tasks \n3. Remove tasks \n4. Exit")
    ch = input("Enter your choice:")
    if ch == '1':
        t = input("Enter the task:")
        tasks.append(t)
        print(f'{t} added successfully.')
    elif ch == '2':
        for i in tasks:
            print(i)
    elif ch == '3':
        tas = input("Enter task to be removed (Case sensitive! Enter task as it is added):")
        if tas in tasks:
            tasks.remove(tas)
            print(f"{tas} removed.")
        else:
            print("Task not found")
    elif ch == '4':
        print("Exiting Todo list")
        break
    else: 
        print("Invalid choice")
