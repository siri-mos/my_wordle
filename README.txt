# **Wordle Python Game**

A simple terminal-based implementation of the popular **Wordle** game in Python.
Guess the five-letter word in **6 attempts** while receiving **color-coded feedback**.

## **Features**

* Automatically installs the **wonderwords** package if it is not already installed.
* Randomly selects a **5-letter English word** as the puzzle key.
* Provides **6 attempts** to guess the correct word.
* Color-coded feedback:

  * **Green** – correct letter in the correct position
  * **Yellow** – letter exists in the word but in a different position
  * **Red** – letter is not in the word
* Fully handles **repeated letters** in both the puzzle and the user’s guesses.
* Validates guesses using the **NLTK English words corpus**.

## **How to Play**

Run the script:

```
python wordle.py
```

When the game starts:

* If the **wonderwords** package is not installed, the script will automatically install it using `pip`.
* You will then be prompted:

  ```
  Enter a five-letter word:
  ```

Enter any valid 5-letter English word and receive color-coded feedback:

* **Green** → correct letter, correct position
* **Yellow** → correct letter, wrong position
* **Red** → letter not in the word

Continue guessing until:

* You guess the word correctly (win), or
* You use all 6 attempts (lose)


## **Code Structure**

* **checkDepPackage()** – Checks if wonderwords is installed
* **installDepPackage()** – Installs wonderwords automatically if missing
* **getPuzzleKey()** – Ensures dependency availability and generates a random puzzle word
* **getLettersCountInWord()** – Counts letters to handle duplicates
* **compare()** – Compares guess to answer and assigns color feedback
* **colorFormatOutput()** – Colors output for display
* **validateInput()** – Validates word length and dictionary presence
* **getValidInputFromUser()** – Prompts repeatedly until a valid word is entered
* **playWordle()** – Main game loop


## **Dependencies**

* **Python 3.x**
* **nltk** – for dictionary validation
* **wonderwords** – for random word generation

  * *Automatically installed at runtime if missing*


## **Notes**

* The game uses ANSI escape sequences for color support.
  Compatible with Linux, macOS, and modern Windows terminals.
* Repeated letters are handled correctly:

  * Exact matches (green) are processed first
  * Yellows appear only when unused instances remain
  * Extra occurrences are marked red

