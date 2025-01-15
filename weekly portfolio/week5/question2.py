import sys

sys.argv = ["count_args.py", "argno1","argno2","argno3","argno4","argno5"]
# Count the number of command line arguments
argument_count = len(sys.argv) - 1  # Exclude the program name
print(f"Number of command line arguments: {argument_count}")

