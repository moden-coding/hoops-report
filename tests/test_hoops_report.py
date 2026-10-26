import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

try:
    import pandas as pd
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "pandas is not installed for the Python running these tests:\n"
        f"    {sys.executable}\n"
        "Select the conda/Anaconda interpreter (Cmd/Ctrl+Shift+P → Python: Select Interpreter), "
        "trash the terminal and open a new one. If you have the extension "
        "'Python Test Explorer for Visual Studio Code', uninstall it and run tests "
        "from the 'Python Tests' tree."
    ) from None

from src.hoops_report import team_count, celtics_scorers, rising_stars

REAL = pd.read_csv(Path(__file__).resolve().parent.parent / "data" / "nba_2024_25.csv")

MINI = pd.DataFrame({
    "Player": ["Ace", "Bolt", "Cruz", "Dash", "Echo", "Finn", "Gage", "Hart"],
    "Team":   ["BOS", "BOS", "NYK", "BOS", "BOS", "LAL", "LAL", "NYK"],
    "Age":    [25, 21, 20, 30, 27, 22, 23, 19],
    "PTS":    [22.0, 15.0, 28.0, 8.0, 16.5, 15.0, 20.0, 6.0],
    "REB":    [5.0, 8.0, 6.0, 3.0, 4.0, 6.0, 6.0, 4.0],
    "AST":    [4.0, 4.0, 4.0, 2.0, 3.5, 4.0, 4.0, 2.0],
})

NOT_A_TABLE = "should return a DataFrame (the filtered table), not a number"


class TestTeamCount(unittest.TestCase):
    def test_real_season(self):
        self.assertEqual(team_count(REAL.copy()), 30,
                         msg="should be the number of different teams in the real season")

    def test_small_table(self):
        self.assertEqual(team_count(MINI.copy()), 3,
                         msg="should be the number of different teams in the small table "
                             "(it has BOS, NYK and LAL)")


class TestCelticsScorers(unittest.TestCase):
    def test_real_season(self):
        result = celtics_scorers(REAL.copy())
        self.assertIsInstance(result, pd.DataFrame, msg=NOT_A_TABLE)
        self.assertEqual(list(result["Player"]),
                         ["Derrick White", "Jaylen Brown", "Jayson Tatum", "Kristaps Porziņģis"],
                         msg="should be every player whose Team is BOS and whose PTS is over 15")

    def test_small_table(self):
        result = celtics_scorers(MINI.copy())
        self.assertIsInstance(result, pd.DataFrame, msg=NOT_A_TABLE)
        self.assertEqual(list(result["Player"]), ["Ace", "Echo"],
                         msg="should only include players who are BOTH on BOS AND over 15 PTS. "
                             "'over 15' means more than 15 — a player with exactly 15 "
                             "shouldn't be included")


class TestRisingStars(unittest.TestCase):
    def test_real_season(self):
        result = rising_stars(REAL.copy())
        self.assertIsInstance(result, pd.DataFrame, msg=NOT_A_TABLE)
        self.assertIn("PRA", result.columns, msg="should have a PRA column")
        self.assertEqual(list(result["Player"]),
                         ["Alperen Sengun", "Amen Thompson", "Brandon Miller", "Josh Giddey",
                          "Keyonte George", "Paolo Banchero", "Shaedon Sharpe",
                          "Victor Wembanyama"],
                         msg="should be every player under 23 with a PRA over 25. "
                             "'under 23' means 22 or younger — 23-year-olds shouldn't be included")
        self.assertEqual([round(pra, 1) for pra in result["PRA"]],
                         [34.3, 26.1, 29.5, 29.9, 26.2, 38.2, 25.8, 39.0],
                         msg="PRA should be PTS + REB + AST")

    def test_small_table(self):
        result = rising_stars(MINI.copy())
        self.assertIsInstance(result, pd.DataFrame, msg=NOT_A_TABLE)
        self.assertIn("PRA", result.columns, msg="should have a PRA column")
        self.assertEqual(list(result["Player"]), ["Bolt", "Cruz"],
                         msg="should be every player under 23 with a PRA over 25. "
                             "'under 23' means 22 or younger, and 'over 25' means more "
                             "than 25 — exact matches shouldn't be included")
        self.assertEqual([round(pra, 1) for pra in result["PRA"]], [27.0, 38.0],
                         msg="PRA should be PTS + REB + AST")


if __name__ == "__main__":
    unittest.main()
