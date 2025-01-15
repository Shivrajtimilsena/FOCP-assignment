password1 = input("Enter a new password (8-12 characters): ")
password2 = input("Re-enter the password: ")

if password1 != password2:
    print("Error: Passwords do not match.")
elif not (8 <= len(password1) <= 12):
    print("Error: Password must be between 8 and 12 characters.")
else:
    print("Password Set")
