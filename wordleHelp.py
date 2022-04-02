
import argparse
from dicthelper import getWords
from wordle import (correct, present, absent)
from wordleSolver import (WordleSolver, HardWordleSolver)

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('length', type=int, help='word length')
    parser.add_argument('--hard', action='store_true', help='play game in hard mode')
    return parser.parse_args()

def formatResponse(r):
    r = r.replace('!', correct)
    r = r.replace('?', present)
    r = r.replace('#', absent)
    return r

def getLines():
    try:
        while True: 
            line = input().lower().split(maxsplit=1)
            if len(line) != 2:
                return
            line[1] = formatResponse(line[1])
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
    print("Indicate correctly placed letters with '!'")
    print("Indicate letters in the wrong place with '?'")
    print("Indicate letters absent from the answer with '#'")
    for g,r in getLines():
        solver.update(g,r)
        print(f'Best guess: {solver.getGuess()}')
    print('\nAll possible words:')
    for g in solver.words:
        print(g)
    
if __name__ == '__main__':
    main()   