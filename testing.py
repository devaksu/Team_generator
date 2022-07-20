from classes import Game, Match
import random
def check_teams(game:Game):
    # ? Testing function
    for i in range(4):
        game.teams[i].goal_difference() 
        game.teams[i].display()


def game_simulator(matches:list, game:Game):
    # ? Testing function 
    for match in matches:
        print(match)
        home = match[0]
        guest = match[1]
        res1 = random.randint(0,2)
        res2 = random.randint(3,4)
        Match(home=game.teams[home], guest=game.teams[guest],result=[res1,res2]).set_scores()
