import random
import re

globalNum_Of_Attempts = 0
globalMaximum_Attempts = 0
globalPrevious_Attempts = []


def start():
    print(f"H A N G M A N\n")


def word_list():
    return "python", "java", "swift", "javascript"


def create_output(response: str, answer: str, final_word: str):
    global globalNum_Of_Attempts
    global globalPrevious_Attempts
    out = list(answer)

    while True:
        if len(response) > 1 or not response:
            print("Please, input a single letter.")
        elif not re.fullmatch(r"[a-z]", response) or response == " ":
            print("Please, enter a lowercase letter from the English alphabet.")
        elif response in globalPrevious_Attempts:
            print("You've already guessed this letter.")
        elif response not in final_word:
            print("That letter doesn't appear in the word")
            globalNum_Of_Attempts += 1
        else:
            globalPrevious_Attempts.append(response)
            response_index = [n for n in range(len(final_word)) if final_word.find(response, n) == n]
            for j in response_index:
                out[j] = response
            globalPrevious_Attempts.append(response)
        return "".join(out)


def main():
    global globalMaximum_Attempts
    global globalNum_Of_Attempts
    global globalPrevious_Attempts

    globalMaximum_Attempts = 8
    play = "Yes"
    wins = 0
    losses = 0

    while play == "Yes":
        start()
        game_type = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        if game_type == "play":
            globalNum_Of_Attempts = 0
            globalPrevious_Attempts = []
            words = word_list()
            final_word = words[random.randint(0, len(words) - 1)]
            user_answer = '-' * len(final_word)
            print(user_answer)
            while globalNum_Of_Attempts < globalMaximum_Attempts:
                res = input("Input a letter:")
                user_answer = create_output(res, user_answer, final_word)
                print(f"\n{user_answer}")
                if user_answer == final_word:
                    print(f"You guessed the word {user_answer}!\nYou survived!")
                    wins += 1
                    globalNum_Of_Attempts = 9
                elif globalNum_Of_Attempts == globalMaximum_Attempts:
                    print("You're hanged!\nYou lost!")
                    losses += 1
                    globalNum_Of_Attempts = 9
        elif game_type == "results":
            print(f"You won: {wins} times.")
            print(f"You lost: {losses} times.")
        elif game_type == "exit":
            play = "No"
            exit()


if __name__ == '__main__':
    main()
