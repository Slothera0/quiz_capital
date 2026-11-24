import unicodedata

def normalize(word):
    word = word.lower()
    word = unicodedata.normalize("NFD", word)
    word = "".join(c for c in word if unicodedata.category(c) != "Mn")
    word = word.replace("-", " ")
    word = word.replace(".", "")
    return word
