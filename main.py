def addTask():
    while True:
        task = input("Enter task: ")
        if task.lower().strip() == "quit":
            break
        with open("todo.txt","a") as file:
            file.write(task +"\n")
            print("Task saved!")
def viewTasks():
    with open ("todo.txt", "r") as file:
        tasks = file.readlines()
        if not tasks:
            print("No tasks saved yet!")
        else:
            for i, task in enumerate(tasks, start = 1):
                print(f"{i}: {task.strip()}")


print("\n\nHello! welcome to your to do list!\n\n")
print("Would you like to add tasks to your to-do list? (yes or no)")
while True:
    in1 = input()
    if in1.lower().strip() == "yes":
        addTask()
        break
    elif in1.lower().strip() == "no":
        break
    else:
        print("\nInvalid response, type yes or no.\n")

while True:
    in2 = input("\nWould you like to view your task list? (yes or no)")
    if in2.lower().strip() == "yes":
        viewTasks()
        break
    elif in2.lower().strip() == "no":
        print("\nAlright, good luck with your plans!\n")
        break
    else:
        print("\ninvalid response, only yes or no\n")