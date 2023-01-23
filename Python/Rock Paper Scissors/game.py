import random

end_game = ['!exit']

user_name = input('Enter your Name: ')
print(f"Hello, {user_name}")
counter = None

action = input().split(',')
lists = action if action != [""] else ['rock', 'paper', 'scissors']
print("Okay, let's start")

rating_file = open("rating.txt")
rating = 0

for line in rating_file:
    name, score = line.split(" ")
    if name == user_name:
        rating = int(score)

while True:
    player_choice = input()
    if player_choice in end_game:
        print("Bye!")
        break
    elif player_choice == '!rating':
        print(f"Your rating: {rating}")
        continue
    elif player_choice not in lists and end_game:
        print("Invalid input")
        continue
    elif player_choice in lists:
        computer_selection = random.choice(lists)
        counter = lists[lists.index(player_choice) + 1:]
        counter += lists[:lists.index(player_choice)]
        counter = counter[:len(counter) // 2]
        if computer_selection in counter:
            print(f"Sorry, but the computer chose {computer_selection}")
        elif player_choice == computer_selection:
            print(f"There is a draw ({player_choice})")
            rating += 50
        else:
            print(f"Well done. The computer chose {computer_selection} and failed")
            rating += 100
