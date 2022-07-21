import random
import data
from classes import Team, Game
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

    
def leaderboard():
    # TODO: Make leaderboard sorting teams based on points and if tied, based on goal difference
    pass


def main(team_count:int=4):
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
    
    #? <------------------------------Testing functions ------------------------------------------->
    #? testing_one_game(match_table, game)
    #? testing_check_teams(game)
    
    

if __name__ == '__main__':
    main()
