def integer(num):
    return 0 <= num <= 100

# Test the function
number = int(input("Enter an integer: "))
if integer(number):
    print("True")
else:
    print("False")
