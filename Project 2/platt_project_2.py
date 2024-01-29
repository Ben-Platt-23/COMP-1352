"""
    Description of program
    Filename: platt_project_2.py
    Author: Ben Platt
    Date: 1/28/24
    Course: COMP-1352
    Assignment: Project 2
    Collaborators: N/A
    Internet Source: W3Schools
"""



import random

def choose_word():
    with open("usaWords.txt") as f:
        words = [word.strip() for word in f.readlines() if len(word.strip()) == 5]
    return random.choice(words)

def calculate_feedback(word, guess):
    feedback = ""
    for i in range(len(word)):
        if guess[i] == word[i]:
            feedback += 'G'
        elif guess[i] in word:
            feedback += 'Y'
        else:
            feedback += 'B'
    return feedback

def play_wordle():
    word_to_guess = choose_word()
    guesses = []
    
    print("Welcome to Wordle! You have six chances to guess the five-letter word.")
    print("A letter G means you got that letter correct and in the right position.")
    print("A letter Y means you matched that letter, but it is in the wrong position.")
    print("A letter B means that letter does not appear in the correct word.")

    for attempt in range(1, 7):
        user_guess = input("What is your guess? ").lower()

        if len(user_guess) != 5 or not user_guess.isalpha():
            print("That is not a valid five-letter word.")
            continue

        guesses.append((attempt, user_guess))
        feedback = calculate_feedback(word_to_guess, user_guess)

        print("Guess {}: {}  {}".format(attempt, user_guess.upper(), feedback))

        if feedback == 'GGGGG':
            print("You win. You got it in {} guesses.".format(attempt))
            break

    else:
        print("You lose, you did not guess the word in 6 guesses.")

play_wordle()