from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "nba_2024_25.csv"


def team_count(df: pd.DataFrame) -> int:
    """How many teams are in the league? Return the number of different teams."""
    pass


def celtics_scorers(df: pd.DataFrame) -> pd.DataFrame:
    """Which Celtics average over 15 points? Return a DataFrame of every player whose Team is BOS and whose PTS is over 15."""
    pass


def rising_stars(df: pd.DataFrame) -> pd.DataFrame:
    """Who are the league's rising stars?
    Add a PRA column (PTS + REB + AST),
    then return a DataFrame of every player under 23 with a PRA over 25."""
    pass


def main():
    df = pd.read_csv(DATA_PATH)
    print("Number of teams:", team_count(df))
    print()
    print("Celtics scoring over 15:")
    print(celtics_scorers(df))
    print()
    print("Rising stars:")
    print(rising_stars(df))


if __name__ == "__main__":
    main()
