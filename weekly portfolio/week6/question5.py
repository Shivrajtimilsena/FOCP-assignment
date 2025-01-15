def simple_encryption(message):
    # Initialize an empty string to store the encrypted message
    encrypted_message = ""
    
    # Iterate through each character in the message and insert 'xy' after each character
    for char in message:
        encrypted_message += char + "xy"  # Add the character followed by 'xy'
    
    return encrypted_message

# Example usage:

# Take user input for the message
message = input("Enter a message to encrypt: ")

# Encrypt the message
encrypted_message = simple_encryption(message)

# Display the encrypted message
print(f"The encrypted message is: {encrypted_message}")
