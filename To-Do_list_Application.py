print ('Hello and welcome to the "Handy-Dandy Ultimate Get r Done to-do list application"!!!')

# This wonderfully handy application will help you get more dont then you ever have before!
# the application will sort and organize all of your task so that you can easily know what 
# you need to get done and track with tasks you have completed!


def mark_as_complete():
    for task in task_list['incomplete']:
        # if no values in list raise error
        print(task)
        print("Would you want to update this task to complete?")
        update = int(input("1 = Yes, 2 = No: "))
        if update == 1:
            if update == 1:
                task_list["complete"].append(task)
                task_list["incomplete"].remove(task)
                print(f"ok great ({task}) has been updated to Complete")
        elif update == 2:
         print("ok next task")



def add_tasks():
    task_list["incomplete"].append(new_task)
    print(f'This is your new task list {task_list["incomplete"]}')



def view_tasks():
    for list , task in task_list.items():
     print(f"{list} {task}")



def rem_incomplete_task():
    for task in task_list["incomplete"]:
        print(task)
        print("would you like to remove task")
        remove = int(input("1 = Yes, 2 = No: "))
    # valueError when using non-numeric character
    # Raise ValueError when selecting number outside of range 
    if option == 1:
        if remove == 1:
            task_list["incomplete"],remove(task)
            print(f"({task}) has been removed from you list.")


def rem_complete_task():
    while true:
        try:
            for task in task_list["complete"]:
                print(task)
                print("would you like to remove task")
                remove = int(input("1 = Yes, 2 = No: "))
                if option not in [1,2]:
                    raise ValueError
        except ValueError:
            print("invalid response please use (1 or 2)")
    # valueError when using non-numeric character
    # Raise ValueError when selecting number outside of range 
        else:
            if option == 1:
                if remove == 1:
                    task_list["complete"],remove(task)
                    print(f"({task}) has been removed from you list.")
                    break




task_list = {"incomplete": [], "complete": []}





while True:

    print('''
    Option Menu:
    1: Add a task
    2: View tasks
    3: Mark a task as complete
    4: Delete a task
    5: Quit ''')
    try:
        option = int(input('Which option would you like to choose( please respond with only 1,2,3,4 or 5): '))
        if option not in [1,2,3,4,5]:
            raise ValueError
    except ValueError:
        print("invalid response please use (1,2,3,4 or 5)")

    # valueError when using non-numeric character
    # Raise ValueError when selecting number outside of range

    if option == 1:
        new_task =input("what task would you like too add?: ")
        add_tasks()
    elif option == 2:
        print("Here are that tasks you have so far. ")
        view_tasks()

    elif option == 3:
        print('which tasks would you like to mark as complete?')
        mark_as_complete()

    elif option == 4:
        print('Do you wish to delete a complete or incomplete task?')
        list= int(input("1 = incomplete , 2 = complete: "))
        if option not in [1,2]:
            raise ValueError
    #except ValueError:
        print("invalid response please use (1 or 2)")

    # valueError when using non-numeric character
    # Raise ValueError when selecting number outside of range 

    if option == 1:
        if list == 1:
            rem_incomplete_task()
        elif list == 2:
            rem_complete_task()
    elif option == 5:
        print("all right good work time to Get'r done!")
        break
