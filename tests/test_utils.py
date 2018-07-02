from utils import is_prediction_line, parse_line

correct_line = "GSW-SAN; 4-1"
incorrect_line = "GSW-SAN; 4-5"


def test_is_prediction_line():
    assert is_prediction_line(correct_line)
    assert is_prediction_line(incorrect_line) is None


def test_parse_line():
    test_result = parse_line(correct_line, True)
    assert test_result.home_team_name == "GSW"
    assert test_result.away_team_name == "SAN"
    assert test_result.home_team_wins == 4
    assert test_result.away_team_wins == 1
