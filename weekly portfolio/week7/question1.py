def unique_sorted_letters(string):
    return sorted(set(string))

# Take user input
message = input("Enter a string: ")

# Get the sorted list of unique letters
result = unique_sorted_letters(message)

# Display the result
print("The sorted list of unique letters is:", result)
