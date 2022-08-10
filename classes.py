from math import floor

class Team():
    """ Class to hold relevant data for each team"""
    def __init__(self, name:str, members:list[str], wins:int=0, points:int=0, games_played:int=0, goals_scored:int=0, goals_against:int=0):
        self.name = name
        self.members = members
        self.wins = wins
        self.points = points
        self.games_played = games_played
        self.goals_scored = goals_scored
        self.goals_against = goals_against
        self.difference = 0

    def goal_difference(self):
        self.difference = self.goals_scored - self.goals_against

    def display(self):
        #? Testing function
        print(f'name {self.name}') 
        print(f'Members {self.members}')
        print(f'wins {self.wins}')
        print(f'points {self.points}')
        print(f'games_played {self.games_played}')
        print(f'Goal difference {self.goals_scored} - {self.goals_against} = {self.difference}')
        print('\n')


class Game():
    """ Class to start a game and add teams to it """
    def __init__(self, points_for_win:int=2):
        self.teams = []
        self.points_for_win = points_for_win

    def add_team(self,team:Team):
        self.teams.append(team)


class Result(Game):
    """ Class to settle scores from matches and update relevant data for scoreboard"""
    def __init__(self, home:Team, guest:Team, result:list[int,int]):
        super().__init__()
        self.home = home
        self.guest = guest
        self.result = result
        self.draw_points = floor(self.points_for_win / 2)

    def set_scores(self) -> None:
        """ Function to set scores after match """
        if self.result[0] == self.result[1]:
            self.home.points += self.draw_points
            self.guest.points += self.draw_points

        elif self.result[0] > self.result[1]:
            self.home.wins += 1
            self.home.points += self.points_for_win
       
        else:
            self.guest.wins += 1
            self.guest.points += self.points_for_win
        
        self.home.goals_scored += self.result[0]
        self.home.goals_against += self.result[1]
        self.home.games_played += 1
        self.home.difference += self.result[0] - self.result[1]

        self.guest.goals_scored += self.result[1]
        self.guest.goals_against += self.result[0]
        self.guest.games_played += 1
        self.guest.difference += self.result[1] - self.result[0]

    def remove_scores(self) -> None:
        """ Function to remove scores after change in match result """
        if self.result[0] == self.result[1]:
            self.home.points -= self.draw_points
            self.guest.points -= self.draw_points

        elif self.result[0] > self.result[1]:
            self.home.wins -= 1
            self.home.points -= self.points_for_win
       
        else:
            self.guest.wins -= 1
            self.guest.points -= self.points_for_win
        
        self.home.goals_scored -= self.result[0]
        self.home.goals_against -= self.result[1]
        self.home.games_played -= 1
        self.home.difference -= self.result[0] + self.result[1]

        self.guest.goals_scored -= self.result[1]
        self.guest.goals_against -= self.result[0]
        self.guest.games_played -= 1
        self.guest.difference -= self.result[1] + self.result[0]



    
