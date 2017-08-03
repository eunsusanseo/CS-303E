#  File: Deal.py

#  Description: Prove that swtiching increases probability of getting prize (Correct guess)

#  Student Name: Eun Seo
 
#  Student UT EID: es29857

#  Course Name: CS 303E

#  Unique Number: 50470

#  Date Created: 10-07-15

#  Date Last Modified: 10-07-15

def main():
    import random
    
    view = 0
    new_guess = 0
    win_by_switching = 0
    
    games = int(input("Enter number of times you want to play: "))
    
    print("\n  Prize      Guess       View    New Guess ", end = " ")
    
    for game in range (games):
        prize = random.randint(1, 3)
        guess = random.randint(1, 3) 
        
        view = random.randint(1,3)
        while (view == prize or view == guess):
            view = random.randint(1,3)
        
        new_guess = random.randint(1,3)
        while (new_guess == view or new_guess == guess):
            new_guess = random.randint(1,3)
            
        print('\n',"{0:>4} {1:>10} {2:>10} {3:>10}".format(prize, guess, view, new_guess), end = " ")
        
        if (new_guess == prize):
            win_by_switching += 1
        
        win_switch = win_by_switching/games
        win_no_switch = 1 - win_switch
    
    print("\n\nProbability of winning if you switch = ", format(win_switch, '.2f'))
    print("Probability of winning if you do not switch = ", format(win_no_switch, '.2f'))  
main()
