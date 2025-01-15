# question3.py

def greet_user():
    # Get the user's name and format it properly
    name = input("Enter your name: ")
    input_name = name.strip().capitalize()  # Capitalize the first letter, lowercase the rest
    print(f"Hello, {input_name}!")

# Call the function to greet the user
greet_user()
