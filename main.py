print("\n\nHello! welcome to your to do list!\n\n")

task = input("Enter task: ")

with open("todo.txt","a") as file:
    file.write(task +"\n")
    print("Task saved!")
    