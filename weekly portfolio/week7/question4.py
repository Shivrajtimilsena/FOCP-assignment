def frequency_analysis(message):
    # Convert the message to lowercase
    message = message.lower()
    
    # Initialize an empty dictionary to store the letter counts
    letter_counts = {}
    
    # Count the frequency of each letter
    for char in message:
        if char.isalpha():  # Only consider alphabetic characters
            if char in letter_counts:
                letter_counts[char] += 1  # Increment count for existing letter
            else:
                letter_counts[char] = 1  # Initialize count for new letter
    
    # Sort the letters by frequency in descending order and get the top 6
    sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)[:6]
    
    # Print the six most common letters and their frequencies
    print("The six most common letters are:")
    for letter, count in sorted_letters:
        print(f"'{letter}': {count}")

# Example usage
message = input("Enter the encrypted message: ")
frequency_analysis(message)
