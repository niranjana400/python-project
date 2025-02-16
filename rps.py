#specific module
#random module
# random num

    # scores

    # while loop
    # player_choice
    # player=computer
    # player=rock
    # player=paper
    # player=scissor
    # else end print the scores break





import random
a = ["Rock", "Paper", "Scissor"]
computer_choice = random.choice(a)

player_score = 0
computer_score = 0
while True:
    player_choice=input("enter your choice")
    if player_choice==computer_choice:
        print("the game is tie")
        player_score+=1
        computer_score+=1

    elif player_choice=="Rock":
          if computer_choice=="Paper":
            print("player wins")
            player_score+=1
          if computer_choice=="Scissor" :
             print("player wins")
             player_score+=1

    elif player_choice=="Paper":
           if computer_choice=="Scissor":
                print("computer wins")
                computer_score+=1
           if computer_choice=="Rock":
                print("player wins")
                player_score+=1

    elif player_choice=="Scissor":
           if computer_choice=="Rock":
                print("computer wins")
                computer_score+=1
           if computer_choice=="Paper":
                print("player wins")
                player_score+=1
    else:
        print("final scores")
        print(player_score)
        print(computer_score)
        break





