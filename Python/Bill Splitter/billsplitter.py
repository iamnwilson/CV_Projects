import random

number_of_friends = int(input("Enter the number of friends joining (including you):\n"))

if number_of_friends <= 0:
    print("No one is joining for the party")
    exit()
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friend_names_and_amounts = [input() for _ in range(number_of_friends)]
    total_bill = float(input("Enter the total bill amount\n"))

answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')

if answer == "Yes":
    split_bill = round(float(total_bill / (number_of_friends - 1)), 2)
    friend_payment = dict.fromkeys(friend_names_and_amounts, split_bill)
    winner = random.choice(friend_names_and_amounts)
    print(f"{winner} is the lucky one!")
    friend_payment[winner] = 0
else:
    split_bill = round(float(total_bill / number_of_friends), 2)
    print("No one is going to be lucky")
    friend_payment = dict.fromkeys(friend_names_and_amounts, split_bill)

print(friend_payment)
