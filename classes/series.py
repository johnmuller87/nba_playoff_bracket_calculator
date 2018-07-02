class Series(object):
    def __init__(self, series_name="",
                 is_result=False,
                 home_team_name="",
                 away_team_name="",
                 home_team_wins=0,
                 away_team_wins=0):

        self.series_name = series_name
        self.is_result = is_result
        self.home_team_name = home_team_name
        self.away_team_name = away_team_name
        self.home_team_wins = home_team_wins
        self.away_team_wins = away_team_wins
