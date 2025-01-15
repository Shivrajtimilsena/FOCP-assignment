import sys

def nl(filename):
    with open(filename, 'r') as file:
        for i, line in enumerate(file, 1):
            print(f"{i}\t{line}", end='')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python nl.py <filename>")
    else:
        nl(sys.argv[1])

 #the command in terminal is question2.py example1.txt example2.txt