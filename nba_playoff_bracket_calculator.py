import os
import re
from utils import parse_line

# Set default variables
THIS_DIRECTORY = os.path.join(os.path.dirname(os.path.realpath(__file__)))


# Read files
def open_input_file(input_file):
    opened_file = open(input_file, "r")
    return opened_file


# Read the rules from the file
def read_rules(input_file):
    correct_teams_rule = 0
    correct_number_of_games_rule = 0
    for line in input_file:
        if re.search("correct teams", line.lower()):
            correct_teams_rule = (int(line.split(';')[1]))
        elif re.search("number of games", line.lower()):
            correct_number_of_games_rule = int(line.split(';')[1])
    return correct_teams_rule, correct_number_of_games_rule


# Read input files; can either be actual results or player predictions
# Boolean is True for results, False for predictions
def read_input_files(input_file, result_or_predictions):
    bracket = [parse_line(line, result_or_predictions) for line in input_file]
    bracket = list(filter(None.__ne__, bracket))
    return bracket


def calculate_points_earned(prediction, result, teams, number_of_games):
    points = 0
    if prediction.series_name == result.series_name:
        points += teams
        if prediction.home_team_wins == result.home_team_wins and prediction.away_team_wins == result.away_team_wins:
            points += number_of_games
    return points


def calculate_player_score(player_predictions, results, teams, number_of_games):
    score = [calculate_points_earned(prediction, result, teams, number_of_games)
             for prediction in player_predictions for result in results]
    return sum(score)


file_location = input("The location of the input file is: ")
print("You entered {}".format(file_location))

playoff_results = open_input_file("{}\\playoff_results_2018.csv".format(THIS_DIRECTORY))
rules = open_input_file("{}\\rules_nba_playoff_brackets.csv".format(THIS_DIRECTORY))
player_input_file = open_input_file("{}\\{}".format(THIS_DIRECTORY, file_location))
actual_results = read_input_files(playoff_results, True)
correct_teams, correct_number_of_games = read_rules(rules)
player_input = read_input_files(player_input_file, False)
player_score = calculate_player_score(player_input, actual_results, correct_teams, correct_number_of_games)

print("Player scored {} points".format(player_score))
