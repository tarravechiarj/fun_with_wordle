
import argparse
from wordle import (Wordle, GameState)
from wordleSolver import HardWordleSolver
from dicthelper import getWords

def solve(game, solver):
    while game.state == GameState.RUNNING:
        guess = solver.getGuess()
        if guess is not None:
            response = game.tryGuess(guess)   
        else:
            print('Solver ran out of guesses')
            break
        solver.update(guess, response)
        print(f'{guess}\n{response}')
    print(game.outcome())


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('length', type=int, help='word length')
    parser.add_argument('--guesses', type=int, default=6, help='number of guesses')
    parser.add_argument('--daily', action='store_true', help='attempt to guess the word of the day')
    return parser.parse_args()

def main():
    args = parseArgs()
    words = getWords(args.length)
    guesses = args.guesses
    daily = args.daily
    game = Wordle(words, guesses=guesses, daily=daily)
    solver = HardWordleSolver(words)
    solve(game, solver)

if __name__ == '__main__':
    main()


