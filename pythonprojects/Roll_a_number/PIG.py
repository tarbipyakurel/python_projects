import random

def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll

while True:
    players=input("Enter the number of players(2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<= players <=4:
            break
        else:    
            print("must be between 2-4 players")
            
    else:
        print("Invalid option")

max_score=50
player_scores=[0 for _ in range (players)]

while max(player_scores)<max_score:
    
    for player_idx in range(players):
        print("\nplayer", player_idx+1, "turn has just started!\n")
        print("Your total score is",player_scores[player_idx],)
        current_score=0
        
        while True:
            should_role=input("would you want to roll(Y/N)? ")
            if should_role.lower()!="y":
                break
            
            value=roll()
            if value==1:
                print("You rolled 1. Turn done")
                current_score=0
                break
            else:
                current_score+=value
                print("You rolled a", value)
                print("You current score is:", current_score)

        player_scores[player_idx]+=current_score
        print("Your total score is", player_scores[player_idx])

max_score=max(player_scores)
winning_index=player_scores.index(max_score)
print("Player number",winning_index+1, "is the winner with score", max_score )
