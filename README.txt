Wordle Python Game

A simple terminal-based implementation of the popular Wordle game in Python.
Guess the five-letter word in 6 attempts while receiving color-coded feedback.

Features

Randomly selects a 5-letter English word as the puzzle key.

Provides 6 attempts to guess the word correctly.

Feedback uses colors to indicate:

Green  – Letter is in the correct position.

Yellow – Letter exists in the word but in a different position.

Red – Letter is not in the word.

Handles repeated letters in both the puzzle and guesses accurately.

Validates guesses against the English dictionary (via NLTK corpus).

Installation

Clone this repository or copy the code into a Python file (e.g., wordle.py).

Install required Python packages:

pip install --upgrade wonderwords nltk


Download NLTK words corpus (one-time setup):

import nltk
nltk.download('words')

How to Play

Run the script:

python wordle.py


The game will prompt:

Enter a five-letter word:


Enter your guess. Feedback will be shown using colors:

Green: Correct letter and position.

Yellow: Letter exists but wrong position.

Red/Black: Letter not in the word.

Continue guessing until:

You guess the word correctly (win), or

You run out of 6 attempts (lose).

Example:

Welcome to Wordle !!
Start guessing the five-letter word, you have 6 attempts!!!
Color Red: Letter is not in the word
Color Yellow: Letter is at a different position in the word
Color Green: Letter is at the same position in the word

Code Structure

getPuzzleKey() – Generates a random 5-letter word.

getLettersCountInWord(word) – Returns a dictionary with the count of each letter in a word.

compare(userGuess, key) – Compares user guess to the puzzle word and returns color codes for feedback.

colorFormatOutput(code, userGuess) – Formats colored output for terminal.

validateInput(userInput) – Checks if input is valid (length & dictionary).

getValidInputFromUser() – Prompts the user until a valid word is entered.

playWordle() – Main game loop.

Dependencies

Python 3.x

wonderwords
 – for random word generation

nltk
 – for dictionary validation

Notes

The game uses ANSI escape codes for terminal colors, which work on most terminals (Linux, macOS, Windows 10+).

Repeated letters are handled correctly:

Greens are prioritized.

Remaining letters are yellow only if unused instances exist.

Extra letters beyond puzzle counts are marked black.