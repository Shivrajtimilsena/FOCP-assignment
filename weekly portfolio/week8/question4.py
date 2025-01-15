import sys

def wc(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        char_count = sum(len(line) for line in lines)
    
    print(f"Lines: {line_count}")
    print(f"Characters: {char_count}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python wc.py <filename>")
    else:
        wc(sys.argv[1])

 #the command in terminal is question4.py example1.txt