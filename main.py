print("****Welcome to my to-do app****")
todos =[]
while True:
    user_option = input("Choose an option below: \n 1. Add \n 2. View \n 3. Edit \n 4. Delete \n 5. Exit \n")
    if user_option == "1":
        # add tasks
        todo = input("Enter to-do:\n")
        todos.append(todo)
        print(f"{todo} has been added successfully")
    elif user_option == "2":
        pass
    elif user_option == "3":
        pass
    elif user_option == "4":
        pass
    elif user_option == "5":
        print("Good Bye...")
        exit()
    else:
        pass

