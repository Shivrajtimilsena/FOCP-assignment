import sys

def spell(filename, dictionary_file="disctionary.txt"):
    with open(dictionary_file, 'r') as dict_file:
        dictionary = set(word.strip().lower() for word in dict_file)

    with open(filename, 'r') as file:
        for line in file:
            for word in line.split():
                word = word.strip().lower()
                if word and word not in dictionary:
                    print(word)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python spell.py <filename>")
    else:
        spell(sys.argv[1])
#the arguments should be line python question5.py example3.txt
"""
the output should be
examelpe.
wards.
crown
pog.

"""

