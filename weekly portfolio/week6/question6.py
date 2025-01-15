def simple_decryption(encrypted_message):
    # Remove 'xy' from the encrypted message
    decrypted_message = encrypted_message.replace("xy", "")
    return decrypted_message

# Example usage:

# Take user input for the encrypted message
encrypted_message = input("Enter the encrypted message: ")

# Decrypt the message
decrypted_message = simple_decryption(encrypted_message)

# Display the decrypted message
print(f"The decrypted message is: {decrypted_message}")
