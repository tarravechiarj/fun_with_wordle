# fun_with_wordle
 CLIs for playing and cheating at a Wordle clone 

wordle.py provides a simple wordle clone class that does no I/O, allowing other python programs to interact with it seamlessly. wordleSolver.py provides a class that can be used to cheat at Wordles, and ordle.py allows the user to play an arbitrary number of Wordle games simultaneously, a la Quordle.

Users can replace the 'dict' text file that Wordle and the solvers use ad their dictionary with their own; the wordle classes should work with 'words' composed of arbitrary non-whitespace characters (though not tests.py).

## Usage example

wordlecli.py:
```sh
python3 wordlecli.py 5 --guesses 6 --hard --daily
```

ordlecli.py:
```sh
python3 ordlecli.py 5 4 9 --daily
```
wordleHelp.py:
```
python3 wordleHelp.py 5
steam !?###
choir ##!##

```
wordleAutosolve.py:
```sh
python3 wordleAutosolve.py 4 --guesses 7 --daily
```
