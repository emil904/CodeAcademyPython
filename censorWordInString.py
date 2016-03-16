def censor(text, word):
    lst = text.split()
    while word in lst:
        index = lst.index(word)
        lst.remove(word)
        lst.insert(index,'*' * len(word))
    return " ".join(lst)