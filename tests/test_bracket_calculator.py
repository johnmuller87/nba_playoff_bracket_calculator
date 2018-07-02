from nba_playoff_bracket_calculator import read_rules, calculate_points_earned, calculate_player_score
from classes.series import Series
import io

prediction1 = Series("HOU-MIA", False, "HOU", "MIA", 4, 1)
prediction2 = Series("HOU-MIA", False, "HOU", "MIA", 4, 3)
prediction3 = Series("HOU-BOS", False, "HOU", "MIA", 4, 1)
list_predictions = [prediction1, prediction2, prediction3]
result = Series("HOU-MIA", True, "HOU", "MIA", 4, 1)


def test_read_rules():
    # Declare some fake data
    rules = "Correct Teams in Series; 6 \n Correct Number of Games; 2"
    rules_file = io.StringIO(rules)
    x1, x2 = read_rules(rules_file)
    assert x1 == 6
    assert x2 == 2


def test_calculate_points_earned():
    points_prediction1 = calculate_points_earned(prediction1, result, 1, 2)
    points_prediction2 = calculate_points_earned(prediction2, result, 1, 2)
    points_prediction3 = calculate_points_earned(prediction3, result, 1, 2)
    assert points_prediction1 == 3
    assert points_prediction2 == 1
    assert points_prediction3 == 0


def test_calculate_player_score():
    score = calculate_player_score(list_predictions, [result], 1, 2)
    assert score == 4
