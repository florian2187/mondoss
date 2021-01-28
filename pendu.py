#/usr/bin/env python2

from random import *

player_score = 0
computer_score = 0
def hangedman(hangman):
    graphic = [
    """
        +-------+
        |
        |
        |
        |
        |
     --------------
     --------------
     """
       ,
     """
        +-------+
        |       |
        |       o
        |
        |
        |
     --------------
     --------------
     """
        ,
     """
        +-------+
        |       |
        |       o
        |       |
        |
        |
     --------------
     --------------
     """
       ,
     """
        +-------+
        |       |
        |       o
        |      -|
        |
        |
     --------------
     --------------
     """
        ,
     """
        +-------+
        |       |
        |       o
        |      -|-
        |
        |
     --------------
     --------------
     """
       ,
     """
        +-------+
        |       |
        |       o
        |      -|-
        |       /
        |
     --------------
     --------------
     """
        ,
     """
        +-------+
        |       |
        |       o
        |      -|-
        |       /\
        |
     --------------
     --------------
     """]
def start():
    print "Jouons au jeu du Pendu."
    while game():
        pass
    scores()
def game():
    dictionary = ["gnu","kernel","linux","mageia","pingouin","ubuntu"]
    word = choice(dictionary)
    word_length = len(word)
    clue = word_length * ["_"]
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_right = 0
    letter_wrong = 0
    global computer_score, player_score
    while (letters_wrong != tries) and ("".join(clue) != word):
        letter=guess_letter()
        if len(letter)==1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print "Vous avez déjà joué la lettre", letter
            else:
                letters_tried = letters_tried + letter
                first_index=word.find(letter)
                if first_index == -1:
                    letters_wrong +=1
                    print "Sorry,",letter,"isn't what we're looking for."
                else:
                    print "Félicitation,",letter,"est correcte."
                    for i in range(word_length):
                        if letter == word[i]:
                            clue[i] = letter
    else:
        print "Faites un autre choix."
    hangedman(letters_wrong)
    print " ".join(clue)
    print "Guesses :", letters_tried
    if letters_wrong == tries:
        print "Fin du jeux."
        print "Le mot était",word
        computer_score +=1
        break

    if "".join(clue) == word:
        print "Gagné !"
        print "le mot était",word
        player_score += 1
        break

    return play_again
def guess_letter():
    print
    letter = raw_input("Devinez le mot mystère :")
    letter.strip()
    letter.lower()
    print
    return letter
def play_again():
    answer = raw_input("Voulez-vous rejouer? o/n: ")
    if answer in ("o","O","oui","Oui","Bien sûr!"):
        return answer
    else:
        print "Merci d'avoir joué, à bientôt!"
def scores():
    global player_score, computer_score
    print "Meilleurs scores"
    print "Joueur :",player_score
    print "Ordinateur :", computer_score

    if __name__ == '__main__':
    start()