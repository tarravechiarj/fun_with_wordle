
import random
from enum import Enum
from datetime import date

correct = '\u2611'    # ballot box with check
present = '\u2610'    # ballot box
absent  = '\u2612'    # ballot box with X

class GameState(Enum):
    RUNNING = 1
    WIN = 2
    LOSE = 3

class Wordle():

    def __init__(self, words, guesses=6, hard=False, daily=False):
        self.words = words
        self.hard = hard
        self.maxGuesses = guesses
        self.resetGame(daily)

    def resetGame(self, daily=False):
        self.guessesLeft = self.maxGuesses
        self.lastGuess = ''
        self.lastResponse = ''
        self.state = GameState.RUNNING
        if daily:
            state = random.getstate()
            random.seed(a=str(date.today()))
            self.answer = random.choice(self.words)
            random.setstate(state)
        else:
            self.answer = random.choice(self.words)
        self.wordlen = len(self.answer)

    def _checkGuess(self, guess):        
        if len(guess) != self.wordlen:
            return f'Guess must be {self.wordlen} letters.'
        elif guess not in self.words:
            return 'Guess not in dictionary.'
        elif self.hard:
            return self._hardCheck(guess)
        else:    
            return None

    def _hardCheck(self, guess):
        for i,(r,g) in enumerate(zip(self.lastResponse, guess)):
            if r == correct and g != self.answer[i]:
                return f"Letter {i + 1} must be '{self.answer[i]}'."
            if r == present and self.lastGuess[i] not in guess:
                return f"'{self.lastGuess[i]}' must be in guess."
        return None

    def _makeResponse(self, guess):
        response = [absent for _ in range(self.wordlen)]
        alist = []
        glist = []
        for i,(g,a) in enumerate(zip(guess,self.answer)):
            if g == a:
                response[i] = correct
            else:
                glist.append((i,g))
                alist.append(a)
        for i,g in glist:
            if g in alist:
                response[i] = present
                alist.remove(g)
        return ''.join(response)

    def tryGuess(self, guess):
        if self.state != GameState.RUNNING:
            return None
        err = self._checkGuess(guess)
        if err is not None:
            return err
        self.lastGuess = guess
        self.lastResponse = self._makeResponse(guess)
        self.guessesLeft -= 1
        if guess == self.answer:
            self.state = GameState.WIN
        elif self.guessesLeft < 1:
            self.state = GameState.LOSE
        return self.lastResponse

    def outcome(self):
        if self.state == GameState.WIN:
            return 'YOU WIN'
        elif self.state == GameState.LOSE:
            return 'YOU LOSE! THE CORRECT ANSWER WAS ' + self.answer
        else:
            return 'GAME RUNNING'

            
