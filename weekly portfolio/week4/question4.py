def remove_last_char(s):
    
    if len(s) > 1: # Check if the string has more than one character
        return s[:-1]  # Remove the last character
    return s  # Return the string unchanged if it's one character or empty

# Test the function
text = input("Enter a string: ")
print(f"New string after removing last character: {remove_last_char(text)}")
