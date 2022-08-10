import random
import data
from classes import Team, Game, Result
from itertools import combinations
from testing import testing_check_teams, testing_game_simulator, testing_one_game


def data_cleaner(peeps:list[str]) -> list[str]:
    """ Clean data (Capitalize and remove whitespaces) """
    participants = []
    for peep in peeps:
        clean = peep.replace(' ','').capitalize()
        participants.append(clean)

    return participants


def team_generator(participants:list[str], team_count:int = 2) -> list[list[str]]:
    """ Get number of teams and divide players randomly to those teams """
    teams = []
    for i in range(team_count):
        teams.append([])
    
    i = 0
    while len(participants) > 0:
        team = i % team_count
        kilpailija = participants.pop(participants.index(random.choice(participants)))
        teams[team].append(kilpailija)
        i += 1
    
    team_names = []
    for team in teams:
        captain = team[0]
        team_names.append("Team "+captain)

    return teams, team_names


def create_game(team_names:list[str], teams:Team, points_for_win:int=2) -> Game:
    """ Create a Game instance """
    game = Game(points_for_win)
    for i in range(len(team_names)):
        t = Team(name=team_names[i], members=teams[i])
        game.add_team(t)
    
    return game


def match_table_maker(team_count:int) -> list[tuple[int,int],list[None,None]]:
    """ Create match table """
    team_numbers = [i for i in range(0,team_count)]
    match_list = list(combinations(team_numbers,2))
    matches = []
    for event in match_list:
        match = [event , [None, None], False]
        matches.append(match)

    return matches
 

def list_games(match_list:list[Team, Team], game) -> None:
    """ Function to show all games and results for played games """
    for count, match in enumerate(match_list, start=1):
        if match[1][0] is None:
            print(f'{count}. {game.teams[match[0][0]].name} \t- {game.teams[match[0][1]].name}')
        else:
            print(f'{count}. {game.teams[match[0][0]].name} \t- {game.teams[match[0][1]].name} \t{match[1][0]} - {match[1][1]}')


def update_result(matches:list[Team, Team], game) -> None:
    """ Update result to match list"""
    list_games(matches,game)
    game_to_update = int(input("Which game you want to update score for?: ")) - 1
    played = matches[game_to_update][2]
    home_team = matches[game_to_update][0][0]
    guest_team = matches[game_to_update][0][1]
    game_result = input("What was the ending result? (separate by dash - ): ").split('-')
    
    if played == False:
        res_home, res_guest = int(game_result[0]), int(game_result[1])
        matches[game_to_update][1][0] = res_home
        matches[game_to_update][1][1] = res_guest
        Result(home=game.teams[home_team], guest=game.teams[guest_team],result=[res_home,res_guest]).set_scores()
        played = True

    else:
        old_home_score = matches[game_to_update][1][0]
        old_guest_score = matches[game_to_update][1][1]
        Result(home=game.teams[home_team], guest=game.teams[guest_team],result=[old_home_score, old_guest_score]).remove_scores()
        res_home, res_guest = int(game_result[0]), int(game_result[1])
        matches[game_to_update][1][0] = res_home
        matches[game_to_update][1][1] = res_guest
        Result(home=game.teams[home_team], guest=game.teams[guest_team],result=[res_home,res_guest]).set_scores()

    list_games(matches, game)


def leaderboard(game, team_count:int) -> None:
    """ Calculate and show leaderboard """
    leaderboard = []
    for i in range(team_count):
        team = game.teams[i]
        leaderboard.append(team)

    for j in range(team_count):
        is_sorted = True
        
        for k in range(team_count - j - 1):
            if leaderboard[k].points == leaderboard[k+1].points:
                if leaderboard[k].difference < leaderboard[k+1].difference:
                    leaderboard[k], leaderboard[k+1] = leaderboard[k+1], leaderboard[k]
                    is_sorted = False

            elif leaderboard[k].points < leaderboard[k+1].points:
                leaderboard[k], leaderboard[k+1] = leaderboard[k+1], leaderboard[k]
                is_sorted = False
        
        if is_sorted:
            break
    
    print(f"Standing \t Team \t\t Games\t Points \t Difference")
    for standing, team in enumerate(leaderboard, start=1):
        if team.difference > 0:
            print(f"{standing}. \t\t {team.name} \t {team.games_played}\t {team.points} \t\t +{team.difference}")
        else:
            print(f"{standing}. \t\t {team.name} \t {team.games_played}\t {team.points} \t\t {team.difference}")


def main():
    # Initial setup
    #*players = input("Players (separated by comma): ").split(',')
    #*team_count = int(input("How many teams will be generated? : "))
    #*points = int(input("How many points for win? (Default 2): "))
    team_count = 4
    players = data.raw_input
    points = 2
    max_teams = len(players) / 2
    
    if team_count < 2 or team_count > max_teams:
        raise ValueError(f"Give number between 2 and {max_teams}")
    
    # Create teams and team names
    cleaned_data = data_cleaner(players)
    teams, team_names = team_generator(cleaned_data, team_count)

    # Start a Game
    game = create_game(team_names,teams, points_for_win=points)
    
    # Create a match
    match_table = match_table_maker(team_count)
    testing_game_simulator(match_table, game)

    #Show match table
    while True:
        num = int(input("1. list games 2. update result 3. show leaderboard: "))
        if num == 1:
            list_games(match_table,game)
        elif num == 2:
            update_result(match_table,game)
        elif num == 3:
            leaderboard(game,team_count)

    
    #? <------------------------------Testing functions ------------------------------------------->
    #? testing_one_game(match_table, game)
    #? testing_check_teams(game)
    
    

if __name__ == '__main__':
    main()
