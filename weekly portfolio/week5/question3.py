import sys
sys.argv = ["shortest_arg.py", "ram", "shyam", "britishcollege", "ok"] #these are the arguments
# Exclude the script name by slicing sys.argv[1:]
arguments = sys.argv[1:]

# Find the shortest argument by sorting the list
if arguments:
    shortest = sorted(arguments, key=len)[0]
    print(f"The shortest argument is: {shortest}")
else:
    print("No arguments provided.")
