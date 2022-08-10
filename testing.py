from classes import Game, Result
import random

def testing_check_teams(game:Game):
    #? Testing function
    for i in range(4):
        game.teams[i].goal_difference() 
        game.teams[i].display()


def testing_game_simulator(matches:list, game:Game):
    #? Testing function
    for match in matches:
        home_team = match[0][0]
        guest_team = match[0][1]
        res1 = random.randint(0,2)
        res2 = random.randint(3,4)
        match[1][0] = res1
        match[1][1] = res2
        
        Result(home=game.teams[home_team], guest=game.teams[guest_team],result=[res1,res2]).set_scores()

def testing_one_game(matches:list, game:Game):
    #? Testing function 
    home_team = matches[0][0][0]
    guest_team = matches[0][0][1]
    res1 = random.randint(0,2)
    res2 = random.randint(3,4)
    matches[0][1][0] = res1
    matches[0][1][1] = res2
    Result(home=game.teams[home_team], guest=game.teams[guest_team],result=[res1,res2]).set_scores()
