import random
from types import NoneType

def data_cleaner(raw_input:list[str]) -> list[str]:
    osallistujat = []
    for peeps in raw_input:
        clean = peeps.replace(' ','').capitalize()
        osallistujat.append(clean)

    return osallistujat


def team_generator(osallistujat:list[str]) -> dict: ### EXTRAS NEED TO BE DONE
    #team_count = int(input("Montako paria arvotaan?: "))
    team_count = 2
    players_per_team = len(osallistujat) // team_count
    extra = len(osallistujat) % team_count
    teams = {}
    for t in range(team_count):
        players = []
        for _ in range(players_per_team):
            new_player = osallistujat.pop(osallistujat.index(random.choice(osallistujat)))
            players.append(new_player)
        
        teams[t] = players
    
    print(teams)  
    return teams


def captains(teams_dict:dict):
    another_dict = {}
    keys = teams_dict.keys()
    for key in keys:
        kapteeni = teams_dict[key][0]
        team_name = "Team " + kapteeni
        print(team_name)
        another_dict[team_name] = teams_dict[key]
    print(another_dict)        


def main():
    #raw_input = input("Anna osallstujat (erota pilkulla): ").split(',')
    raw_input = ["aksu ", "jussi", "ilta ", "havi", "casti", "hoppe", "Ve ge", "Ryyppö ", " jules"]
    cleaned_data = data_cleaner(raw_input)
    teams = team_generator(cleaned_data)
    captains(teams)

if __name__ == '__main__':
    main()