print("Comb's command")
print("Type help to see commands")

while True:
    command = input(">>> ")

    if command == "help":
        print("Commands: help, echo, clear, exit,")

    elif command.startswith("echo "):
        print(command[5:])

    elif command == "clear":
        import os
        os.system("cls")

    elif command == "exit":
        print("Goodbye!")
        break

    else:
        print("Unknown command")
