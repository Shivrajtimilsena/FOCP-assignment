import sys

def main():
    # Check if command-line arguments are provided
    if len(sys.argv) < 2:
        print("Error: No temperature readings provided.")
        print("Usage: python script_name.py temp1 temp2 temp3 ...")
        return

    try:
        # Convert command-line arguments to a list of floats
        temperatures = list(map(float, sys.argv[1:]))
        
        # Calculate maximum, minimum, and mean                       
        maximum = max(temperatures)
        minimum = min(temperatures)
        mean = sum(temperatures) / len(temperatures)
        
        # Display results
        print(f"Maximum Temperature: {maximum}")
        print(f"Minimum Temperature: {minimum}")
        print(f"Mean Temperature: {mean:.2f}")
    except ValueError:
        print("Error: All arguments must be numbers.")
        print("Usage: python script_name.py temp1 temp2 temp3 ...")

if __name__ == "__main__":
    main()



"""
you have to give command-line argument like this "python script_name.py 34 34 45 67 78 22 44 "
"""