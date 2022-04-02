
import random
from datetime import date
from wordle import (Wordle, GameState)

GameState = GameState

class Ordle():

    def __init__(self, words, numGames, guesses, daily=False):
        if daily:
            state = random.getstate()
            random.seed(a=str(date.today()))
            self.wordles = [Wordle(words, guesses=guesses) for _ in range(numGames)]
            random.setstate(state)
        else:
            self.wordles = [Wordle(words, guesses=guesses) for _ in range(numGames)]
        self.state = GameState.RUNNING

    def _getResponses(self, guess):
        responses = []
        for w in self.wordles:
            r = w.tryGuess(guess)
            responses.append(r if r else w.lastResponse)
        return responses

    def tryGuess(self, guess):
        responses = self._getResponses(guess)
        states = [w.state for w in self.wordles]
        if GameState.RUNNING not in states:
            if GameState.LOSE in states:
                self.state = GameState.LOSE
            else:
                self.state = GameState.WIN
        return responses

