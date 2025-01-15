def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

# Take user input as an integer
number = int(input("Enter an integer to find its factors: "))

# Call the function and print the result
print(f"The factors of {number} are:", find_factors(number))
