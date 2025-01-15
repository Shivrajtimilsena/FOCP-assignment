def manage_country_capitals():
    capitals = {}  # Dictionary to store country and capital city
    
    while True:
        # Ask the user to enter the name of a country
        country = input("Enter a country (or 'exit' to quit): ").strip()
        
        # Handle termination condition
        if country.lower() == 'exit':
            print("Exiting the program.")
            break
        
        # Normalize the country name to handle case-insensitivity
        country_lower = country.lower()
        
        # Check if we already know the capital of the country
        if country_lower in capitals:
            print(f"The capital city of {country} is {capitals[country_lower]}.")
        else:
            # If the capital is unknown, ask the user to enter it
            capital = input(f"Enter the capital city of {country}: ").strip()
            capitals[country_lower] = capital  # Store the capital with the lowercase country key
            print(f"Thanks! The capital of {country} is now recorded as {capital}.")
    
    # Optionally, display all stored capitals when the user exits
    print("\nStored capitals:")
    for country, capital in capitals.items():
        print(f"{country.capitalize()}: {capital}")

# Run the program
manage_country_capitals()
