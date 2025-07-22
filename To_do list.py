def to_do_list():
    tasks=[]

    while True:
        print("1.Add task")
        print("2.Remote task")
        print("3.Show task")
        print("4.Exit")
        choice = input("Enter your choice:")

        if choice == "1":
            task = input("Enter task:")
            tasks.append(task)
        elif choice == "2":
            task = input("Enter task to remote:")
            if task in tasks:
                tasks.remote(task)
            else:
                print("Task not found")
        elif choice == "3":
            print("Tasks: ")
            for task in tasks:
                print("-" + task)
        elif choice == "4":
            break
        else:
            print("invalid choice")

to_do_list()