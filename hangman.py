import random
import re

# Function checks if the string contains any special character
def run(newstring):


    unwantedCharactersList = re.compile("[@_!#$%^&*('<>?/\|}{~:]")
    
    # Pass the string in search 
    # method of regex object.    
    if(unwantedCharactersList.search(newstring) == None):
        return True
        
    else:
        return False

filename = "/usr/share/dict/british-english"


#variable that is assigned by grabbing words from the dictionary file 
DictionaryWords = ([x.strip().lower() for x in open(filename,"r")])


#list of words that make it past the filter stage (no special characters)
validwords = []

invalidwords = []

specialCharactersChecker = []


c = 0

#loop to run until valid words has 100 items
for i in range(len(DictionaryWords)):
    specialCharactersChecker.append(DictionaryWords[i])

    newstring = (''.join(specialCharactersChecker))

    specialCharactersChecker.clear()

    #checkpoint-works well up to here so far
    if run(newstring) and 12 > len(newstring) > 4:
        #adding the grabbed word to the valid word list if it has no special characters
        validwords.append(newstring)
        newstring = newstring.replace('',newstring)
   
    elif run(newstring) == False:
        invalidwords.append(newstring)
        newstring = newstring.replace('',newstring)

        
#print(validwords)



#stages of lives left in ascending order

Graphics = [r'''
------------           ___    ___   _____     _     _        ____        _    ______    _____
|         |            | |    | |  / ____ \  | |   | |      | ___ \     | |  |  ____|  |  __ \   
|          O            \ \  / /  | |    | | | |   | |      | |  \ \    | |  | |       | |  \ \ 
|         / |            \ \/ /   | |    | | | |   | |      | |   \ \   | |  | |___    | |   \ \   
|          |              |  |    | |    | | | |   | |      | |    | |  | |  |  ___|   | |    | |  
|         / |             |  |    | |____| | | |___| |      | |____| |  | |  | |____   | |____| |  
|                         |__|     \______/   \_____/       |________|  |_|  |______|  |________|  ''',r'''
------------
|         |
|          O 
|         / |
|          |
|         / 
|          ''',r'''
------------
|         |
|          O 
|         / |
|          |
|          
|          ''',r'''
------------
|         |
|          O 
|         / |
|          
|          
|          ''',r'''
------------
|         |
|          O 
|         / 
|          
|          
|          ''',r'''
------------
|         |
|          O 
|         
|          
|          
|           ''',r'''
------------
|         |
|           
|         
|          
|          
|           ''',r'''
''',r'''
''',r'''
''',r'''
''']



enteredletterlist = []

word = (random.choice(validwords)).lower()

guesslen = len(word)

totallives = len(word)

print("you have",totallives,"lives or you die")

hiddenword = ["_"]*len(word)

while guesslen > 0 and totallives > 0:

    guess = (input("guess a letter: ")).lower()


    while guess in enteredletterlist or guess.isalpha() == False or len(guess) > 1:
        if guess in enteredletterlist:
            print("you've already entered that letter")
            guess = input("guess another letter ")
        elif guess.isalpha() == False:
            guess = input("error, give me a letter this time: ")
        elif len(guess) > 1:
            guess = input("only one letter ")
    
    count = word.count(guess)

    for eachletter in word:
        if guess == eachletter:
            i = word.index(eachletter)
            hiddenword[i] = guess
        else:
            for position, letter in enumerate(word):
                if letter == guess:
                    hiddenword[position] = guess

    enteredletterlist.append(guess)
    
    if count > 0 and guesslen > 0:
        guesslen -= count 
        print("correct!",totallives,"lives left")    
    else:
        totallives -= 1
        print("wrong, you have",totallives,"lives left")    
    
    print(Graphics[totallives])
    print(*hiddenword) 
    

    
  
if guesslen == 0:
    print("congratulations, hangman survives! The word is",word)       
if totallives == 0:
    print(" ")
    print("you died. The word was",word)
    print(" ")