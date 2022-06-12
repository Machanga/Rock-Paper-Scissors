import random

def rock_paper_scissors():
    try:
        player = int(input("Pick a choice (1 = rock, 2 = paper, 3 = scissors): "))
    except:
        print('Kindly pick 1, 2, or 3: (1=rock, 2=paper, 3=scissors)')
        player = int(input("Pick a choice (1 = rock, 2 = paper, 3 = scissors): "))
        
    # possible_choices = [1, 2, 3] so omputer picks at random from the three
    computer = random.randint(1,3)
    
    print(f"\nYou chose {player}, computer chose {computer}.\n")

    if player == computer:
        print(f"Both players selected {player}. It's a tie!")
    elif player == 1:
        if computer == 3:
            print("Rock smashes scissors! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    elif player == 2:
        if computer == 1:
            print("Paper covers rock! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player == 3:
        if computer == 2:
            print("Scissors cuts paper! You win!")
        else:
            print("Scissors cuts paper!! You lose.")
            
rock_paper_scissors()