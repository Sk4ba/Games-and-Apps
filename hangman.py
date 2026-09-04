import random

lives = 5

#words and randomizing
word = random.choice(["epstein", "bitch", "faggot", "league"])
redacted_word = ["_"] * len(word)

#funcs
def menu():
    print("====================================")
    print("              hangman               ")
    print("====================================")

def win():
    print("====================================")
    print("              you win               ")
    print("====================================")

def lose():
    print("====================================")
    print("              you lose              ")
    print("====================================")

menu()
print(f"Word: {''.join(redacted_word)}")

while(lives > 0):
    guess = input("Enter letter: ").lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                redacted_word[i] = guess
    else:
        lives -= 1
    print(f"Word: {''.join(redacted_word)}")

    if ''.join(redacted_word) == word:
        break

if lives > 0:
    win()
else:
    lose()