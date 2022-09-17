import random

def take_input():               # function which checks the user input if correct
    empty_spaces = 30           # number of empty spaces inside the else msg
    while True:
        entry = str(input("Choose [r]ock, [s]cissors or [p]aper, [end] to exit: "))
        if entry in ["r", "s", "p", "end"]:
            return entry
            break
        else:
            print(f"{' '* empty_spaces}Invalid option, choose [r], [s] or [p], [end] to exit:\n")

def give_output(result):        # function which interprets the result
    empty_spaces = 53           # number of empty spaces inside the result
    if result == "L":
        return f"{' '* empty_spaces}Loss\n"
    elif result == "W":
        return f"{' '* empty_spaces}Win\n"
    elif result == "D":
        return f"{' '* empty_spaces}Draw\n"

all_results = []                # accumulate the history

while True:
    user_input = take_input()
    if user_input == "end":
        break

    computer_choice = random.choice("rsp")
    # print(computer_choice, end=" ")         # tester durign game develop giving the computer choice
                                              # remove the first bracket to see the computer choice

    # main logic section below ........
    #
    if computer_choice == "r" and user_input == "s":
        result = "L"
    elif computer_choice == "s" and user_input == "p":
        result = "L"
    elif computer_choice == "p" and user_input == "r":
        result = "L"
    elif computer_choice == user_input:
        result = "D"
    else:
        result = "W"

    all_results.append(result)              # saves entries inside history

    print(give_output(result))              # calls function give_output to interpret the output

# output section below ...........
if all_results == []:
    print(f'End Game\n')
else:
    print()
    print(f"Won Games: {all_results.count('W')}   Lost Games: {all_results.count('L')}   Drawn Games: {all_results.count('D')}")
    print(f"History: {', '.join(all_results)}")
