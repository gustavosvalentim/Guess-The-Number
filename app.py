import random


player_name = input('Hey, what\'s your name? ')

print('Hello ' + player_name + ', welcome to the guess the number.')
print('It\'s a number between 1 and 20.')
print('Try to guess')

while True:

   secret = random.randint(1, 20)
    guesses_taken = 0
    guess = 0

    while guess != secret:
        guess = input('')

        if guess != '':
            guess = int(guess)

        else:
            continue

        guesses_taken += 1

        if guess == secret:
            print('Congratulations ' + player_name + ', you did it in ' + str(guesses_taken) + ' times.')

        else:
            if guess > secret:
                print('Try with minor number.')

            elif guess < secret:
                print('Try a higher number.')

            continue

    final_choice = input('Do you want to play again?[Y/N] ')

    while final_choice.capitalize() != 'Y' and final_choice.capitalize() != 'N':
        print('Invalid option.')
        final_choice = input('Do you want to play again?[Y/N] ')

    if final_choice.capitalize() != 'Y':
        break
