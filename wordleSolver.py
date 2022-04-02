
import wordle

wildcard = '\n'

class WordleSolver():

    def __init__(self, words):
        wordlen = len(words[0]) if words else 0
        self.words = words
        self.template = [wildcard for _ in range(wordlen)]
        self.absent = [set() for _ in range(wordlen)]
        self.misplaced = dict()
        self.words.sort(key=lambda w: len(set(w)), reverse=True)

    def update(self, guess, response):
        grs = list(zip(guess,response))
        self.misplaced = dict()
        for (g,r) in grs:
            if r == wordle.present:
                self.misplaced.setdefault(g,0)
                self.misplaced[g] += 1
        for i,(g,r) in enumerate(grs):
            if r == wordle.correct:
                self.template[i] = g
            elif g in self.misplaced:
                self.absent[i].add(g)
            else:
                for s in self.absent:
                    s.add(g)
        self.words = list(filter(self._wordFilter, self.words))
                        
    def _wordFilter(self, word):
        for i,l in enumerate(word):
            if self.template[i] == wildcard and l not in self.absent[i]:
                continue
            elif self.template[i] != l:
                return False
        for m,c in self.misplaced.items():
            if c > word.count(m):
                return False
        return True

    def getGuess(self):
        if not self.words:
            return None
        elif len(self.words) == 1:
            return self.words[0]
        else:
            pickfrom = []
            n = len(set(self.words[0]))
            for w in self.words:
                if len(set(w)) < n:
                    break
                pickfrom.append(w)
            lscores = self._countLetters()
            return max(pickfrom, key=lambda w: lscores[w])

    def _countLetters(self):
        lcounts = dict()
        lscores = dict()
        for word in self.words:
            for l in word:
                lcounts.setdefault(l,0)
                lcounts[l] += 1
        for word in self.words:
            s = 0
            for l in word:
                s += lcounts.get(l,0)
            lscores[word] = s
        return lscores


class HardWordleSolver(WordleSolver):
    """
    This class is slightly optimized to follow hard mode rules. It is not meant
    to be used interactively, as its words list will become inaccurate if updated
    with non-hard mode guesses.
    """
    def _wordFilter(self, word):
        added = dict()
        for i,l in enumerate(word):
            if self.template[i] == wildcard and l not in self.absent[i]:
                added.setdefault(l,0)
                added[l] += 1
            elif self.template[i] != l:
                return False
        for m,c in self.misplaced.items():
            if c > added.get(m, 0):
                return False
        return True
