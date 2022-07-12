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
        return 0
    if (computer_choice =='rock' and user_choice =='paper') or (computer_choice =='paper' and user_choice =='scissors') or (computer_choice =='scissors' and user_choice =='rock'):
        print('User wins!')
        return 1
    else:
        print('Computer wins!')
        return 2

def get_overall_winner(score):
    if score[1]==score[2]:
        print("Draw overall!")
        return
    if score[1]>score[2]:
        print("User wins overall!")
        return
    print("Computer wins overall!")

def play(total_rounds):
    rounds = 1
    score = [0,0,0] # count of draws, user wins, computer wins
    while rounds<=total_rounds:
        print(f"Start round {rounds}")
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        score[get_winner(computer_choice, user_choice)]+=1
        rounds+=1

    get_overall_winner(score)
    return

play(5)