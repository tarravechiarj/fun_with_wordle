
def getWords(size):
    words = []
    with open('dicts/dict') as f:
        for w in f:
            w = w.rstrip()
            if len(w) == size:
                words.append(w)
    return words
