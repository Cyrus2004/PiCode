def decorator_function(original_function):
    def wrapper_function():
        print("Hello.")
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print("I did nothing!")

def file():
    text = open("I_did_something!", "w")

while True:
    command = input()

    if command == "don't do anything!":
        display()

    if command == "do something!":
        file()

    if command != "a" and command != "b":
        print("Big error!")