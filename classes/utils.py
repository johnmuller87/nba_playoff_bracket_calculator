import re
from classes.series import Series


class Utils:
    def __init__(self):
        self.data = []

    def is_prediction_line(line):
        pattern = "^\w{3}-\w{3};\s[0-4]-[0-4]"
        return re.match(pattern, line)

    def parse_line(line, result_or_prediction):
        if Utils.is_prediction_line(line):
            teams, result = line.split(';')
            home_team, away_team = teams.split('-')
            home_team_wins, away_team_wins = result.split('-')
            return Series(teams, result_or_prediction, home_team, away_team, int(home_team_wins), int(away_team_wins))
