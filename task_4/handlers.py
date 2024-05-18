import re

contacts = {}

def input_error_decorator_factory(
        args_length = 0,
        args_error_msg = "Enter the argument for the command"):
    def input_error(func):
        def inner(*args, **kwargs):
            try:
                if (len(args) < args_length):
                    raise ValueError(args_error_msg)
                
                return func(*args, **kwargs)
            except(ValueError, IndexError, KeyError) as err:
                print(f"Error: {err}")
        return inner
    return input_error

def say_greeting():
    print("How can I help you?")        

@input_error_decorator_factory(args_length = 2, args_error_msg = "Enter name and phone number to add")
def add_contact(name: str, phone: str) -> None:
    contacts[name] = normalize_phone(phone)
    print("Contact added.")

@input_error_decorator_factory(args_length = 2, args_error_msg = "Enter name and phone number to update")
def change_contact(name: str, phone: str) -> None:
    if name not in contacts:
        raise ValueError("Contact is not found")

    contacts[name] = normalize_phone(phone)
    print("Contact updated.")

@input_error_decorator_factory(args_length = 1, args_error_msg = "Enter the name")
def show_phone(name: str) -> str:
    if name not in contacts:
        raise ValueError("Contact is not exist")

    return contacts[name]

def show_all() -> dict:
    return contacts


def normalize_phone(phone_number: str) -> str:
    country_code = "38"
    pattern = r"[+\d]"
    phone_number = "".join(re.findall(pattern, phone_number))

    if not phone_number.startswith("+"):
        phone_number = re.sub(fr"^({country_code})?", f"+{country_code}", phone_number)

    if len(phone_number) != 13:
        raise ValueError(f"Invalid phone number: {phone_number}")

    return phone_number