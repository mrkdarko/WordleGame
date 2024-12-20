import os
import colorama
import random
from colorama import Fore, Back, Style
from wordlist_helper import getWordList
os.system('color 7') #white

def wordlechecker(letters, lettersofGuess):
    temp1 = letters.copy()
    temp2 = lettersofGuess.copy()
    colorcheck=[-1,-1,-1,-1,-1]

    for i in range(0, len(letters)):
        if temp1[i].upper() == temp2[i].upper():
            colorcheck[i]=2
            from colorama import Fore, Back, Style
            temp1[temp1.index(temp2[i])]="Done"
            temp2[i]="Done"
    for x in range(0,len(letters)):
        if temp2[x]=="Done":
            colorcheck[i]=2
        elif temp2[x]!= "Done" and temp2[x] in temp1 and colorcheck[x]!=2:
            from colorama import Fore, Back, Style
            colorcheck[x]=1
            temp1[temp1.index(temp2[x])]="Done"
            temp2[x]="Done"
        else:
            colorcheck[x]=-1
            from colorama import Fore, Back, Style
    temp1= letters
    return colorcheck

def wordleprinter(list,lettersOfGuess):
    for x in range(0,len(letters)):
        if list[x]== -1:
            print(Back.RED + lettersOfGuess[x].upper(), end = " ")
        if list[x]==1:
            print(Back.YELLOW + lettersOfGuess[x].upper(), end = " ")
        if list[x]==2:
            print(Back.GREEN + lettersOfGuess[x].upper(), end = " ")

if __name__ == "__main__":
    bigwordlist=[]
    bigwordlist = getWordList()
    bigwordlistai = bigwordlist.copy()
    word = []
    word.append((random.choice(bigwordlist)).upper())
    letters=[]
    print("Welcome to Wordle!")
    print("Begin By Typing a 5-Letter Word...")
    aisetup= str(input("DO YOU WANT TO PLAY AGAINST AN AI?"))
    if aisetup.upper()=="NO":
        for i in range(0,len(word[0])):
            letters.append(word[0][i].lower())
        for z in range(1,7):
            userInitialGuess = str(input(Back.BLUE + "Guess " + str(z) + ": ")).lower()
            while len(userInitialGuess) != 5 or (userInitialGuess not in bigwordlist):
                print("this word is invalid!")
                userInitialGuess = str(input(Back.BLUE + "Guess " + str(z) + ": ")).lower()
            move = []
            move.append(userInitialGuess)
            lettersOfGuess=[]
            for x in range(0,len(move[0])):
                lettersOfGuess.append(move[0][x].lower())
            list=[]
            list= wordlechecker(letters,lettersOfGuess)
            wordleprinter(list,lettersOfGuess)
            print()
            if letters ==lettersOfGuess:
                print("You Got the Word!")
                print("You Won In: " + str(z) + " Guesses!")
                break
            if z==6 and letters!=lettersOfGuess:
                print("You Lost the Game")
                print("The word was: " + str(word))
    if aisetup.upper()=="YES":
        for i in range(0,len(word[0])):
            letters.append(word[0][i].lower())

    print(Style.RESET_ALL)


#########################################################
