import random
import hangman_words


print(''' 
 _                                              
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  
''')

stages = [''' 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
'''  
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''  
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''  
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''  
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''  
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''  
  +---+
  |   |
      |
      |
      |  
      |    
=========
''']
lives = 6

word_lists = hangman_words.hangman_words
chosen_word = random.choice(word_lists)

placeholder = ""
placeholder += "_"* len(chosen_word)
print(f"Word to guess =  {placeholder}")

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You have already guessed {guess}.")
    display = ""

    for letter in chosen_word:
        lives = lives
        if letter == guess:
            display += letter 
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter   
        else:
            display += "_"
    print(display)  
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    print(stages[lives])
    if lives > 0:
        stars = "*"*30
        print(stars + f"{lives}/6 LIVES LEFT" + stars)
    if lives == 0:
       game_over = True
       print(stars + f"IT WAS {chosen_word}! YOU LOSE." + stars)

    if "_" not in display:
        game_over = True
        print("You win.")    
