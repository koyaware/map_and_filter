words = ("apple", "banana", "cherry")

def words_len(word):
    return list(map(lambda i: len(i),word))
print(words_len(words))