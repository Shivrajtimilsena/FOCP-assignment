def simple_encrypt(message):
    message = message.replace(" ", "")  # Remove all spaces
    encrypted_message = message[::-1]   # Reverse the message
    return encrypted_message

# Take user input as a string
message = input("Enter a message to encrypt: ")

# Call the function and print the result
print(f"The encrypted message is: {simple_encrypt(message)}")
