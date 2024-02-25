"""
    Description of program
    Filename: project_1.py
    Author: Ben Platt
    Date: 1/16/24
    Course: COMP-1352
    Assignment: Project 1
    Collaborators: N/A
    Internet Source: W3Schools
"""






import random

def generate_number():
    """
        Description of function
        parameters: None
        return: outputs the randomized number
    """
    digits = [str(i) for i in range(10)]
    random.shuffle(digits)
    return ''.join(digits[:3])

def evaluate_guess(secret_number, guess):
    """
        Description of function
        parameters: secret_number, guess
        return: outputs the pico and fermi counts
    """
    fermi_count = 0
    pico_count = 0

    for i in range(3):
        if guess[i] == secret_number[i]:
            fermi_count += 1
        elif guess[i] in secret_number:
            pico_count += 1

    return fermi_count, pico_count

def is_valid_guess(guess):
    """
        Description of function
        parameters: guess
        return: outputs whether the guess was valid or not
    """
    return len(set(guess)) == len(guess)

def play_game():
    """
        Description of function
        parameters: None
        return: Outputs the actual game or gameplay and provides the interactive parts including the instructions and result
    """
    secret_number = generate_number()
    attempts = 0

    print("Welcome to Pico Fermi Bagels!")
    print("Try to guess the three-digit number with no repeating digits.")

    while True:
        guess = input("Enter your guess: ")

        if not is_valid_guess(guess):
            print("Invalid guess! Make sure to enter a number with no repeated digits.")
            continue

        attempts += 1

        fermi, pico = evaluate_guess(secret_number, guess)

        if fermi == 3:
            print("Fermi! Fermi! Fermi!")
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif fermi > 0:
            print(f"Fermi! " * fermi, end="")
        elif pico > 0:
            print(f"Pico! " * pico, end="")
        else:
            print("Bagels!")


play_game()