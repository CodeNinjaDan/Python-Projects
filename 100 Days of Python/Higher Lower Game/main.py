import random

from orca.orca import start

from game_data import data
#1. Art
#2. Function -> Randomly choose characters from dict inside a list in game_data
#       -> Display the chosen characters as A and B
#       -> If pick_a and pick_b are the same, place them in a while loop to pick again
#3. Display for the user to pick who has more followers
#   -> When displaying, show the person's name, what they do and where they're from(Retrieve from the nested dictionary)
#4. Win function -> If the user_guess == random choice :
#       then B moves to a and the next person to guess is displayed
#       the game goes on until the user loses.
#
# pick_a = random.choice(data)
# follower_values_a = pick_a['follower_count']
# print(f"Compare A: {pick_a['name']}, a {pick_a['description']}, from {pick_a['country']}")
#
# pick_b = random.choice(data)
# while pick_b == pick_a:
#     pick_b = random.choice(data)
# follower_values_b = pick_b['follower_count']
# print(f"Against B: {pick_b['name']}, a {pick_b['description']}, from {pick_b['country']}")

def guess():
    pick_a = random.choice(data)
    follower_values_a = pick_a['follower_count']
    print(f"Compare A: {pick_a['name']}, a {pick_a['description']}, from {pick_a['country']}")

    pick_b = random.choice(data)
    while pick_b == pick_a:
        pick_b = random.choice(data)
    follower_values_b = pick_b['follower_count']
    print(f"Against B: {pick_b['name']}, a {pick_b['description']}, from {pick_b['country']}")
    score = 0
    start_game = True
    user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    while start_game:
        if user_answer == "A" and follower_values_a > follower_values_b:
            pick_a = pick_b
            follower_values_a = follower_values_b
            pick_b = random.choice(data)
            while pick_b == pick_a:
                pick_b = random.choice(data)
            score += 1
        elif user_answer == "B" and follower_values_b > follower_values_a:
            pick_a = pick_b
            follower_values_a = follower_values_b
            pick_b = random.choice(data)
            while pick_b == pick_a:
                pick_b = random.choice(data)
            score += 1
        else:
            print(f"Sorry, that's wrong. score: {score}")
            start_game = False

guess()