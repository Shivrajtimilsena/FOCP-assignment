def letters_in_at_least_one(word1, word2):
    return sorted(set(word1) | set(word2))  # Union of both sets
def letters_in_both(word1, word2):
    return sorted(set(word1) & set(word2))  # Intersection of both sets
def letters_in_either_but_not_both(word1, word2):
    return sorted(set(word1) ^ set(word2))  # Symmetric difference of both sets
word1 = "cheese"
word2 = "cheer"

print("Letters in at least one:", letters_in_at_least_one(word1, word2))  # Union
print("Letters in both:", letters_in_both(word1, word2))  # Intersection
print("Letters in either but not both:", letters_in_either_but_not_both(word1, word2))  # Symmetric difference
