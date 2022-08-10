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


def create_game(team_names:list[str], teams) -> Game:
    """ Create a Game instance """
    game = Game()
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
        match = [event , [None, None]]
        matches.append(match)

    return matches
 

def list_games(match_list:list[Team, Team], game):
    """ Function to show all games and results for played games """
    for count, match in enumerate(match_list, start=1):
        if match[1][0] is None:
            print(f'{count}. {game.teams[match[0][0]].name} - {game.teams[match[0][1]].name}')
        else:
            print(f'{count}. {game.teams[match[0][0]].name} - {game.teams[match[0][1]].name} {match[1][0]} - {match[1][1]}')


def update_result(matches:list[Team, Team], game):
    """ Update result to match list"""
    list_games(matches,game)
    game_to_update = int(input("What game you want to update score for?: ")) - 1
    game_result = input("What was the ending result? (separate by dash - ): ").split('-')
    home_team = matches[game_to_update][0][0]
    guest_team = matches[game_to_update][0][1]
    res_home, res_guest = int(game_result[0]), int(game_result[1])
    matches[0][1][0] = res_home
    matches[0][1][1] = res_guest
    Result(home=game.teams[home_team], guest=game.teams[guest_team],result=[res_home,res_guest]).set_scores()
    list_games(matches, game)


def leaderboard(game, team_count):
    """ Calculate and show leaderboard """
    # TODO: Notice goal difference
    leaderboard = []
    for i in range(team_count):
        team = game.teams[i]
        leaderboard.append(team)

    for j in range(team_count):
        is_sorted = True
        
        for k in range(team_count - j - 1):
            if leaderboard[k].points < leaderboard[k+1].points:
                leaderboard[k], leaderboard[k+1] = leaderboard[k+1], leaderboard[k]
                is_sorted = False
        
        if is_sorted:
            break
    
    print(f"Sijoitus \t Joukkue \t Pisteet \t Maaliero")
    for standing, team in enumerate(leaderboard, start=1):
        print(f"{standing}. \t\t {team.name} \t {team.points} \t\t {team.difference}")


def main(team_count:int=4):
    # Initial setup
    #*raw_input = input("Anna osallistujat (erota pilkulla): ").split(',')
    #*team_count = int(input("Montako joukkuetta arvotaan?: "))
    
    # Create teams and team names
    cleaned_data = data_cleaner(data.raw_input)
    teams, team_names = team_generator(cleaned_data, team_count)

    # Start a Game
    game = create_game(team_names,teams)
    
    # Create a match
    match_table = match_table_maker(team_count)
    testing_game_simulator(match_table, game)

    #Show match table
    list_games(match_table,game)
    update_result(match_table,game)
    leaderboard(game,team_count)

    
    #? <------------------------------Testing functions ------------------------------------------->
    #? testing_one_game(match_table, game)
    #? testing_check_teams(game)
    
    

if __name__ == '__main__':
    main()
