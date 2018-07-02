import re
from classes.series import Series


def is_prediction_line(line):
    pattern = "^\w{3}-\w{3};\s[0-4]-[0-4]"
    return re.match(pattern, line)


# Returns None for non prediction lines
def parse_line(line, is_result):
    if is_prediction_line(line):
        teams, result = line.split(';')
        home_team, away_team = teams.split('-')
        home_team_wins, away_team_wins = result.split('-')
        return Series(teams, is_result, home_team, away_team, int(home_team_wins), int(away_team_wins))
