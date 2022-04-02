
import unittest
import wordle
import dicthelper

c = wordle.correct
a = wordle.absent
p = wordle.present

class WordleTest(unittest.TestCase):

    def setUp(self):
        self.words = dicthelper.getWords(5)

    def test_guesses(self):
        w = wordle.Wordle(self.words, guesses=6)
        w.answer = 'apple'
        self.assertEqual(w.tryGuess('qwert'), 'Guess not in dictionary.')
        self.assertEqual(w.tryGuess('any'), 'Guess must be 5 letters.')
        self.assertEqual(w.tryGuess('broom'), ''.join([a,a,a,a,a]))
        self.assertEqual(w.tryGuess('steam'), ''.join([a,a,p,p,a]))
        self.assertEqual(w.tryGuess('point'), ''.join([p,a,a,a,a]))
        self.assertEqual(w.tryGuess('alarm'), ''.join([c,p,a,a,a]))
        self.assertEqual(w.tryGuess('apple'), ''.join([c,c,c,c,c]))   
        self.assertEqual(w.tryGuess('apple'), None)  


    def test_states(self):
        w = wordle.Wordle(self.words, guesses=6)
        w.answer = 'apple'
        self.assertEqual(w.state, wordle.GameState.RUNNING) 
        self.assertEqual(w.tryGuess('apple'), ''.join([c,c,c,c,c])) 
        self.assertEqual(w.state, wordle.GameState.WIN) 
        w.resetGame() 
        w.answer = 'apple'
        for _ in range(w.maxGuesses):
            self.assertEqual(w.tryGuess('trees'), ''.join([a,a,p,a,a]))
        self.assertEqual(w.state, wordle.GameState.LOSE)

    def test_daily(self):
        ws = [wordle.Wordle(self.words, daily=True) for _ in range(10)]
        self.assertTrue(all([w.answer == ws[0].answer for w in ws]))

    def test_hard(self):
        w = wordle.Wordle(self.words, guesses=6, hard=True)
        w.answer = 'apple'
        self.assertEqual(w.tryGuess('steam'), ''.join([a,a,p,p,a]))
        self.assertEqual(w.tryGuess('alarm'), "'e' must be in guess.")
        self.assertEqual(w.tryGuess('alert'), ''.join([c,p,p,a,a]))
        self.assertEqual(w.tryGuess('point'), "Letter 1 must be 'a'.")
        self.assertEqual(w.guessesLeft, 4)
        self.assertEqual(w.tryGuess('apple'), ''.join([c,c,c,c,c]))

if __name__ == '__main__':
    unittest.main()
