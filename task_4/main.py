import handlers

commands = ["hello", "add", "change", "phone", "all", "exit", "close"]

def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command == "hello":
            handlers.say_greeting()

        elif command == "add":
            handlers.add_contact(*args)

        elif command == "change":
            handlers.change_contact(*args)

        elif command == "phone":
            name = args[0]
            phone = handlers.show_phone(name)

        elif command == "all":
            contacts = handlers.show_all()
            print(contacts)

        elif command in ["exit", "close"]:
            print("Goodbye!")
            break

        else:
            print("Invalid command.")
            print(f"Existed commands: {commands}")

if __name__ == "__main__":
    main()