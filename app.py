import random
import data

def data_cleaner(peeps:list[str]) -> list[str]:
    # Clean data (Capital letters and remove whitespace)
    osallistujat = []
    for peep in peeps:
        clean = peep.replace(' ','').capitalize()
        osallistujat.append(clean)

    return osallistujat

def team_generator(osallistujat:list[str], team_count:int = 2) -> list[list[str]]:
    """Get number of teams and divide players randomly to those teams"""
    teams = []
    for i in range(team_count):
        teams.append([])
    
    i = 0
    while len(osallistujat) > 0:
        team = i % team_count
        kilpailija = osallistujat.pop(osallistujat.index(random.choice(osallistujat)))
        teams[team].append(kilpailija)
        i += 1

    return teams

def print_teams(teams:list[list[str]]) -> None:
    for team in teams:
        print('Team ' + team[0])
        for player in team:
            print(player)
        print('\n')

def main():
    #raw_input = input("Anna osallstujat (erota pilkulla): ").split(',')
    #team_count = int(input("Montako paria arvotaan?: "))
    team_count = 4
    cleaned_data = data_cleaner(data.raw_input)
    teams = team_generator(cleaned_data, team_count)
    print_teams(teams)

if __name__ == '__main__':
    main()