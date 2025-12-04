#pip install --upgrade wonderwords

from wonderwords import RandomWord
import builtins # Import builtins to access the original input function
import nltk
nltk.download('words')
from nltk.corpus import words
from enum import Enum

#one time definitions
PUZZLE_WORD_LEN = 5
MAX_ATTEMPTS = 6
errCode = Enum('errCode', [('LEN_MORE_THAN_PUZZLE_LEN', 1),('LEN_LESS_THAN_PUZZLE_LEN', 2), ('NOT_FOUND_IN_DICT', 3)])

def getPuzzleKey():
  randWord = RandomWord()
  # generate a random word
  puzzleKey = randWord.word(word_min_length=PUZZLE_WORD_LEN, word_max_length=PUZZLE_WORD_LEN)
  return puzzleKey

def getLettersCountInWord(word):
  lettersCount = {}
  for i in range(len(word)):
    lettersCount[word[i]] = word.count(word[i])
  return lettersCount

def compare(userGuess, key):
  code = {}
  #get the letter count in the puzzle key to track repeated letters
  keyLetterCount = getLettersCountInWord(key)
  print(keyLetterCount)  
  for i in range(PUZZLE_WORD_LEN):
    if(userGuess[i] == key[i] and keyLetterCount[userGuess[i]] > 0):
      code[i] = '\033[32m' #Green
      keyLetterCount[userGuess[i]] = keyLetterCount[userGuess[i]] - 1
    elif(userGuess[i] in key):
      if(keyLetterCount[userGuess[i]] > 0):
        code[i] = '\033[33m' #Yellow
        keyLetterCount[userGuess[i]] = keyLetterCount[userGuess[i]] - 1
      else:
        code[i] = '\033[31m' #Black
    else:
      code[i] = '\033[31m' #Black
  return code

def colorFormatOutput(code, userGuess):
  out = ''
  for i in range(len(code)):
    out = out + code[i] + userGuess[i] + '\033[0m'
  return out

def validateInput(userInput):
  if(len(userInput) > PUZZLE_WORD_LEN):
    return errCode.LEN_MORE_THAN_PUZZLE_LEN
  elif(len(userInput) < PUZZLE_WORD_LEN):
    return errCode.LEN_LESS_THAN_PUZZLE_LEN
  else: #check if the word is valid english word
    try:
      if (userInput.lower() in words.words()):
        return userInput.lower()
      else:
        return errCode.NOT_FOUND_IN_DICT
    except:
      return errCode.NOT_FOUND_IN_DICT
    else:
      return userInput.lower()

def getValidInputFromUser():
  userInput = builtins.input(" Enter a five letter word:")
  userInput = validateInput(userInput)
  while(userInput in [errCode.LEN_MORE_THAN_PUZZLE_LEN, errCode.LEN_LESS_THAN_PUZZLE_LEN, errCode.NOT_FOUND_IN_DICT]):
    if(userInput == errCode.LEN_MORE_THAN_PUZZLE_LEN):
      print("The word is longer than the allowed: ", PUZZLE_WORD_LEN , "please enter a valid word")
    elif(userInput == errCode.LEN_LESS_THAN_PUZZLE_LEN):
      print("The word is too short, retry!")
    elif(userInput == errCode.NOT_FOUND_IN_DICT):
      print("The word is not in the dictionary, retry!")
    else:
      return userInput
    userInput = builtins.input(" Enter a five letter word:")
    userInput = validateInput(userInput)
  return userInput

def playWordle():
  
  print("Welcome to Wordle !!\nStart guessing the five letter word, you have 6 attempts!!!")
  print("Color Red: Letter is not in the word")
  print("Color Yellow: Letter is at a different position in the word")
  print("Color Green: Letter is at the same position in the word")
  attemptCount = MAX_ATTEMPTS
  #get the puzzle key for the game
  key = getPuzzleKey()
  
  guess = getValidInputFromUser()
  while(guess != key ):
    colorCode = compare(guess, key)
    print(colorFormatOutput( colorCode, guess))
    if (attemptCount -1):
      attemptCount = attemptCount - 1
      print("You have", attemptCount , "attempt(s) left")
      guess = getValidInputFromUser()
    else:
      print("Sorry, you ran out of your 6 attempts! Word was: ", key)
      break
  if (guess == key):
    print("Congratulations, you solved the puzzle!!\033[32m", key, '\033[0m')

#start the game!
playWordle()