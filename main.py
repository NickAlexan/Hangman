import random
import pictures

voc = ['hello', 'world', 'cat', 'dog']
word = random.choice(voc)



num_of_let = len(word)

blank = []

for i in range(num_of_let):
    blank += "_"

print(blank)

print(''.join(blank))
tries = 7

game_over = False

while not game_over:
    guess = input("Enter the letter: ").lower()
    if blank.count(guess) > 0:
        tries -= 1
        print(f"{pictures.stages[tries]}\nYou already guess {guess} letter. You have {tries} tries left")
    if word.count(guess) > 0:
        for index in range(num_of_let):
            if word[index] == guess:
                blank [index] = guess
        print(blank)
        if "_" not in blank:
            print(f"You win, the word is {word}")
            game_over = True
    else:

        tries -= 1
        if tries == 0:
            game_over = True
            print(f"{pictures.stages[tries]}\nYou lose, the word is {word}")

        else:
            print(f"{pictures.stages[tries]}\nWrong, you have {tries} tries left")


