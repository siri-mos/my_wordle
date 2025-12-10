import subprocess
import sys
from wonderwords import RandomWord
import builtins # Import builtins to access the original input function
import nltk
nltk.download('words', quiet=True)
from nltk.corpus import words
from enum import Enum

#one time definitions
PUZZLE_WORD_LEN = 5
MAX_ATTEMPTS = 6
errCode = Enum('errCode', [('LEN_MORE_THAN_PUZZLE_LEN', 1),('LEN_LESS_THAN_PUZZLE_LEN', 2),('NOT_FOUND_IN_DICT', 3),('DEP_INSTALL_FAILED', 4)])
colorCode = Enum('colorCode', [('YELLOW', '\033[33m'),('GREEN', '\033[32m'), ('RED', '\033[31m'), ('RESET', '\033[0m')])
    
def checkDepPackage():
  try:
    import wonderwords
  except ImportError:
    return False
  return True

def installDepPackage(package):
    try:
      subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])
      print("installing")
    except subprocess.CalledProcessError as e:
      print("Failed to install ", package, "!! Error returned: ", e)
      return errCode.DEP_INSTALL_FAILED

def getPuzzleKey():
  #check and install 'wonderwords' - a package we need to generate the puzzle key
  if (checkDepPackage() == False):
    if (installDepPackage("wonderwords") == errCode.DEP_INSTALL_FAILED):
      return errCode.DEP_INSTALL_FAILED
  randWord = RandomWord()
  # generate a random word
  while(True):
    puzzleKey = randWord.word(word_min_length=PUZZLE_WORD_LEN, word_max_length=PUZZLE_WORD_LEN).lower()
    if(puzzleKey in words.words()):
      return puzzleKey

def getLettersCountInWord(word):
  lettersCount = {}
  for i in range(len(word)):
    lettersCount[word[i]] = word.count(word[i])
  return lettersCount

def compare(userGuess, key):
  code = {k:'\033[31m' for k in range(PUZZLE_WORD_LEN)}
  userMatchDone = {k: 0 for k in range(PUZZLE_WORD_LEN)}
  #get the letter count in the puzzle key to track repeated letters
  keyLetterCount = getLettersCountInWord(key)
  for i in range(PUZZLE_WORD_LEN):
    if(userGuess[i] == key[i] ):
      code[i] = colorCode.GREEN.value
      keyLetterCount[userGuess[i]] = keyLetterCount[userGuess[i]] - 1
      userMatchDone[i] = 1
  for i in range(PUZZLE_WORD_LEN):
    if (userMatchDone[i] != 1):   
      if(userGuess[i] in key):
          if(keyLetterCount[userGuess[i]] > 0):
            code[i] = colorCode.YELLOW.value
            keyLetterCount[userGuess[i]] = keyLetterCount[userGuess[i]] - 1
          else:
            code[i] = colorCode.RED.value
      else:
        code[i] = colorCode.RED.value
  return code

def colorFormatOutput(code, userGuess):
  out = ''
  for i in range(len(code)):
    out = out + code[i] + userGuess[i] + colorCode.RESET.value
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

def getValidInputFromUser():
  userInput = builtins.input(" Enter a five letter word:")
  userInput = validateInput(userInput)
  while(userInput in [errCode.LEN_MORE_THAN_PUZZLE_LEN, errCode.LEN_LESS_THAN_PUZZLE_LEN, errCode.NOT_FOUND_IN_DICT]):
    if(userInput == errCode.LEN_MORE_THAN_PUZZLE_LEN):
      print("The word is longer than the allowed, retry!")
    elif(userInput == errCode.LEN_LESS_THAN_PUZZLE_LEN):
      print("The word is shorter the required, retry!")
    elif(userInput == errCode.NOT_FOUND_IN_DICT):
      print("The word is not in the dictionary, retry!")
    else:
      return userInput
    userInput = builtins.input(" Enter a five letter word:")
    userInput = validateInput(userInput)
  return userInput

def playWordle():
  attemptCount = MAX_ATTEMPTS
  #get the puzzle key for the game
  key = getPuzzleKey()
  if (key == errCode.DEP_INSTALL_FAILED):
    print("Unable to install the depedant pakcage, Exiting!!")
    return
  print("Welcome to Wordle !!\nStart guessing the five letter word, you have 6 attempts!!!")
  print("Color Red: Letter is not in the word")
  print("Color Yellow: Letter is at a different position in the word")
  print("Color Green: Letter is at the same position in the word")
  guess = getValidInputFromUser()
  while(guess != key ):
    output = compare(guess, key)
    print(colorFormatOutput( output , guess))
    if (attemptCount > 1):
      attemptCount = attemptCount - 1
      print("You have", attemptCount , "attempt(s) left")
      guess = getValidInputFromUser()
    else:
      print("Sorry, you ran out of your 6 attempts! Word was: ", key)
      break
  if (guess == key):
    print("Congratulations, you solved the puzzle!!", colorCode.GREEN.value, key, colorCode.RESET.value)


#start the game!
playWordle()
