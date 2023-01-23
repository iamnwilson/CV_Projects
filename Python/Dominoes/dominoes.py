import itertools
import random

domino_set = []
stock_pieces = []
computer_pieces = []
player_pieces = []
domino_snake = []
player_status = ""
for i, j in itertools.product(range(7), range(7)):
    if [j, i] not in domino_set:
        domino_set.append([i, j])
computer_max_pair = []
player_max_pair = []
while True:
    random.shuffle(domino_set)
    stock_pieces = domino_set[:14]
    computer_pieces = domino_set[14:21]
    player_pieces = domino_set[21:]
    computer_max = 0
    player_max = 0

    for i in range(7):
        if computer_pieces[i][0] == computer_pieces[i][1] and computer_max < computer_pieces[i][0]:
            computer_max = computer_pieces[i][0]
        if player_pieces[i][0] == player_pieces[i][1] and player_max < player_pieces[i][0]:
            player_max = player_pieces[i][0]

    if computer_max > player_max:
        player_status = 'player'
        domino_snake.append([computer_max, computer_max])
        computer_pieces.remove([computer_max, computer_max])
        break
    elif player_max > computer_max:
        player_status = 'computer'
        domino_snake.append([player_max, player_max])
        player_pieces.remove(([player_max, player_max]))
        break

print("=" * 70)
print(f"Stock size: {len(stock_pieces)}")
print(f"Computer pieces: {len(computer_pieces)}")
print(domino_snake)
for index, domino in enumerate(player_pieces):
    print(f"{index + 1}:{domino}")
