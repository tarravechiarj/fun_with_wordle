
import argparse
from dicthelper import getWords
from wordleSolver import (WordleSolver, HardWordleSolver)

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('length', type=int, help='word length')
    parser.add_argument('--hard', action='store_true', help='play game in hard mode')
    return parser.parse_args()

def getLines():
    try:
        while True: 
            line = input().lower().split(maxsplit=1)
            if len(line) != 2:
                return
            yield tuple(line)
    except EOFError:
        return
        
def main():
    args = parseArgs()
    words = getWords(args.length)
    if args.hard:
        solver = HardWordleSolver(words)
    else:
        solver = WordleSolver(words)
    print('Enter: {guess} {response}')
    for g,r in getLines():
        solver.update(g,r)
        print(f'Best guess: {solver.getGuess()}')
    print('\nAll possible words:')
    for g in solver.words:
        print(g)
    
if __name__ == '__main__':
    main()   