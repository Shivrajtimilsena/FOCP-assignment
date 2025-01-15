import sys

def diff(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        content1 = f1.read()
        content2 = f2.read()

    if content1 == content2:
        print("The files are the same.")
    else:
        print("The files are different.")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python diff.py <file1> <file2>")
    else:
        diff(sys.argv[1], sys.argv[2])
