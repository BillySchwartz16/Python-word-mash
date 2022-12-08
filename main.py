import random
import time

# Define the constants
MAX_WORDS = 10
MAX_TIME = 60

# Choose a word to be used as the base
words = ["apple", "banana", "orange", "strawberry", "grape"]
word = random.choice(words)

# Initialize the game state
words_created = []
score = 0
time_left = MAX_TIME

# Define the starting time of the game
start_time = time.time()

# Print the initial state
print("Word:", word)
print("Words created:", words_created)
print("Score:", score)
print("Time left:", time_left)

# Play the game until the player reaches the maximum number of words or the timer reaches 0
while len(words_created) < MAX_WORDS and time_left > 0:
    # Ask the player for a new word
    new_word = input("Create a new word using the letters in the word above: ")

    # Update the game state
    if all(letter in word for letter in new_word) and len(new_word) > 1 and new_word not in words_created:
        words_created.append(new_word)
        score += 1
    else:
        print("Invalid word!")
    time_left = MAX_TIME - int(time.time() - start_time)

    # Print the current state
    print("Word:", word)
    print("Words created:", words_created)
    print("Score:", score)
    print("Time left:", time_left)

# Print the final state
if len(words_created) >= MAX_WORDS:
    print("You reached the maximum number of words! Your final score is:", score)
else:
    print("Time's up! Your final score is:", score)


# Play the game until the player quits
while True:
    # Play the game
    play_game()

    # Ask the player if they want to play again
    response = input("Do you want to play again? (Y/N) ")
    if response.lower() != "y":
        break

# Print a goodbye message
print("Thank you for playing! Goodbye.")