from random import choice

# computer picks a choice at random, user uses text input, comparison and winner is output

def get_computer_choice():
    return choice(['rock','paper','scissors'])

def get_user_choice():
    while True:
        userchoice = input("Enter your choice: ")
        if userchoice.lower() in ('rock','paper','scissors'):
            return userchoice

def get_winner(computer_choice, user_choice):
    print(f'Computer chose {computer_choice}, User chose {user_choice}')
    if computer_choice == user_choice:
        print('Draw!')
        return
    if (computer_choice =='rock' and user_choice =='paper') or (computer_choice =='paper' and user_choice =='scissors') or (computer_choice =='scissors' and user_choice =='rock'):
        print('User wins!')
    else:
        print('Computer wins!')
    return

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)
    return

play()