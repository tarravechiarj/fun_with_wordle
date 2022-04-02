
import argparse
import sys
from ordle import (Ordle, GameState)
from dicthelper import getWords

def run(ordle):
    print('ENTER GUESS:')
    while ordle.state == GameState.RUNNING:
        g = input().lower()
        rs = ordle.tryGuess(g)
        print('\n'.join(rs))
    for w in ordle.wordles:    
        print(w.outcome())

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('length', type=int, help='word length')
    parser.add_argument('games', type=int, help='number of wordle games to play simultaneously')
    parser.add_argument('guesses', type=int, help='number of allowed guesses')
    parser.add_argument('--daily', action='store_true', help='attempt to guess the word of the day')
    return parser.parse_args()

def main():
    args = parseArgs()
    words = getWords(args.length)
    game = Ordle(words, args.games, guesses=args.guesses, daily=args.daily)
    try:
        run(game)
    except (KeyboardInterrupt, EOFError):
        sys.exit('Quitting')

if __name__ == '__main__':
    main()
