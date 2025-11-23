
tasks = []
import json
import os 

# File name for saving tasks
FILE_NAME = "tasks.json"
# ---- Load tasks from file when program starts ----
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []  # Return empty list if file does not exist

# ---- Save tasks to file ----
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

        # ---- Load tasks on start ----
tasks = load_tasks()


while True:
    print('\n--- To-Do Menu ---')
    print('1. Add Task')
    print('2. View Task')
    print('3. Delete Task')
    print('4. Mark Task as Done')
    print('5. Exit')

    choice = input('Enter Choice: ')

    # Add task

    if choice == '1':
        task = input('Enter Task Name: ')
        tasks.append({"name": task, "done": False})
        save_tasks()
        print ('Task added!')

    # View tasks

    elif choice == '2':
        if len(tasks) == 0:
            print('No tasks found.')
        else:
            print('\nYour Tasks:')
            for i, t in enumerate(tasks, start=1):
                status = 'Done' if t['done'] else 'Pending'
                print(f"{i}. {t['name']} [{status}]")

    # Delete task
                
    elif choice == '3':
        if len(tasks) == 0:
            print('No tasks to delete.')
        else:
            print('\nYour Tasks:')
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t['name']}")
                try:
                    task_num = int(input('Enter task number to delete: '))
                    index = task_num - 1

                    if 0 <= index < len(tasks):
                        removed = tasks.pop(index)
                        save_tasks()
                        print(f'Task {removed} deleted!')

                    else:
                        print('Invalid task nubmer.')
                except ValueError:
                    print('Please enter a valid number.')




    # Mark task done
    elif choice == '4':
        if len(tasks) == 0:
            print('No tasks to mark.')
        else:
            print('\nYour Tasks:')
            for i, t in enumerate(tasks, start=1):
                status = 'Done' if t['done'] else 'Pending'
                print(f"{i}. {t['name']} [{status}]")
        try:
            task_num = int(input('Enter task nummber to mark: '))
            index = task_num - 1

            if 0 <= index <len(tasks):
                tasks [index]['done'] = True
                save_tasks()
                print(f'Task {tasks[index]['name']} marked as DONE!') 
            else:
                print('Invalid task number.')
        except ValueError:
            print('Please enter a valid number.')



    elif choice == '5':
        print('Exiting Program... Good Bye!')
        break #stop the loop program end
    else:
        print('Invalid option, please try again')











