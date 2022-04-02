
import argparse
import sys
from wordle import (Wordle, GameState)
from dicthelper import getWords

def run(wordle):
    print('ENTER GUESS:')
    while wordle.state == GameState.RUNNING:
        g = input().lower()
        print(wordle.tryGuess(g))
    print(wordle.outcome())

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('length', type=int, help='word length')
    parser.add_argument('--guesses', type=int, default=6, help='number of guesses')
    parser.add_argument('--hard', action='store_true', help='play game in hard mode')
    parser.add_argument('--daily', action='store_true', help='attempt to guess the word of the day')
    return parser.parse_args()

def main():
    args = parseArgs()
    words = getWords(args.length)
    game = Wordle(words, hard=args.hard, guesses=args.guesses, daily=args.daily)
    try:
        run(game)
    except (KeyboardInterrupt, EOFError):
        sys.exit('Quitting')

if __name__ == '__main__':
    main()
