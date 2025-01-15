def integer_to_binary(n):
    if n == 0:
        return '0'
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

# Take user input as an integer
number = int(input("Enter a positive integer: "))

# Call the function and print the result
print("The binary representation of", number, "is:", integer_to_binary(number))
