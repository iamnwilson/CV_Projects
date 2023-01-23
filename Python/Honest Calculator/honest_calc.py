msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]


def is_one_digit(v):
    try:
        if v.is_integer() and -10 < v < 10:
            return True
        else:
            return False
    except:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (int(v1) == 1 or int(v2) == 1) and v3 == "*":
        msg += msg_7
    if (int(v1) == 0 or int(v2) == 0) and (v3 in "*-+"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)


memory = 0.0
while True:
    try:
        x, operator, y = input(msg_[0]).split()
        x = memory if x == 'M' else float(x)
        y = memory if y == 'M' else float(y)
        check(x, y, operator)
        if operator not in ["+", "-", "/", "*"]:
            print(msg_2)

        if operator == "+":
            result = x + y
        elif operator == "-":
            result = x - y

        elif operator == "*":
            result = x * y

        elif operator == "/":
            result = x / y
        print(result)
        answer = input(msg_4)
        if answer == 'y':
            if is_one_digit(result):
                msg_index = 10
                while msg_index < 13:
                    ans = input(msg_[msg_index])
                    if ans == "y":
                        msg_index += 1
                        if msg_index == 12:
                            memory = result
                    else:
                        break

            else:
                memory = result
        ask_user = input(msg_5)
        if ask_user == "n":
            break

    except ValueError:
        print(msg_1)
    except ZeroDivisionError:
        print(msg_3)
