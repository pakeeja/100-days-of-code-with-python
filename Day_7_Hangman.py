from replit import clear 
import random
import hangman_words
import hangman_art
word_list=hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)
display = []
for _ in range(word_length):
    display += "_"
while not end_of_game:
    guess = input("Guess a letter: \n").lower()
    clear()

    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}\n")
    if guess not in chosen_word:
        lives -= 1
        
        if lives == 0:
            end_of_game = True
            print(f"OOPS!! The word was {chosen_word}")
            print("You lose.")
        else:
            print(f"You have guessed {guess}, that's not in the word. You lose a life !!")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])