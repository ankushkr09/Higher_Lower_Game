import random   #import random module
from game_data import data   #import game_data file
from art import logo, vs     #import art file
import os       #import os





def clear_screen():
    """Clear screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

# Call the clear_screen function to clear the screen
clear_screen()




#define a function to retrieve data from dictionary
def account_data(account):
    """Format the data to readable format"""
    account_name = account['name']
    account_desc = account['description']
    account_place = account['country']
    return (f"{account_name}, a {account_desc}, from {account_place}.")

#define a function to compare the user guess against both accounts followers count
def check_result(guess, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        if guess == 'a':
            return True
        else:
            return False
    if b_follower_count > a_follower_count:
        if guess == 'b':
            return True
        else:
            return False

print(logo)
game_over = False    #flag
score = 0    #assign score to 0
account_b = random.choice(data)    #randomly choosing a dictionary(account) from data list
while  not game_over:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    #from dictionary taking out followers_count of both the randomly chosen account
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    
    print(f"Compare A: {account_data(account_a)}")
    print(vs)
    print(f"Against B: {account_data(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    #checking wether user's guess is correct or not and saving it to a variable 'is_correct'
    is_correct = check_result(guess, a_follower_count, b_follower_count)

    clear_screen()
    print(logo)
    #if user's guess is correct
    if is_correct == True:
        score += 1   #increase the score with 1
        print(f"You're right! Current score: {score}.")
    #if user's guess is wrong
    else:
        print(f"Sorry, that's wrong. Final score: {score}")   #print them final score
        game_over = True   #change the flag to True and end the while loop
    


