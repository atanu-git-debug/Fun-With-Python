import random

def guessing_game(user,user_name,computer_name):
    computer = random.randint(1,10)
    user = user

    winner = user_name if user == computer else computer_name

    return f"{user_name} chose: {user}, {computer_name} chose: {computer}.\nWinner is: {winner}"

def get_name():

    name = input("Enter your name: ")

    computer_name = input("You want to set a name for computer? (yes/no): ")

    c_name = input("Enter the computer's name: ") if computer_name.lower() == "yes" else "Computer"

    return name, c_name

def get_guess_from_user():

    user = int(input("Enter a number between 1 and 10: "))
    return user

# the main function
if __name__ == "__main__":

    names = get_name()
    user_input = get_guess_from_user()
    result = guessing_game(user_input,names[0],names[1])
    print(result)
