words = ["Anna","Alexey","Alia","Kazak","Dom"]
def palindromes(word):
    word = map(lambda i:i.lower(), word)
    return list(filter(lambda x: x == x[::-1], word))
print(palindromes(words))