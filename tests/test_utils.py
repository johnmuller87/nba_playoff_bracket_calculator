from classes.utils import Utils


def test_is_prediction_line():
    assert Utils.is_prediction_line("GSW-SAN; 4-1")
    assert Utils.is_prediction_line("GSW-SAN; 4-5") is None


def test_parse_line():
    test_result = Utils.parse_line("HOU-MIN; 4-1", True)
    assert test_result.home_team_name == "HOU"
    assert test_result.away_team_name == "MIN"
    assert test_result.home_team_wins == 4
    assert test_result.away_team_wins == 1
