import math

def is_prime(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # Other even numbers are not prime
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False  # If divisible by any number, it's not prime
    return True  # If no factors found, it's prime

# Take user input as an integer
number = int(input("Enter an integer to check if it's prime: "))

# Call the function and print the result
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
