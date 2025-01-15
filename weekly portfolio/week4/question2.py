def count_case(s):
    uppercase = sum(1 for c in s if c.isupper())
    lowercase = sum(1 for c in s if c.islower())
    return uppercase, lowercase

# Test the function
text = input("Enter a string: ")
upper, lower = count_case(text)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")
