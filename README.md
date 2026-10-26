# Hoops Report

Answer three questions about the 2024–25 NBA season, one function each.

## Your data

One row per player. **Team** is a 3-letter abbreviation (BOS = Boston Celtics). The stats are per-game averages: **PTS** points, **REB** rebounds, **AST** assists. **Age** is the player's age.

## The questions

All three functions are in `src/hoops_report.py`.

1. **How many teams are in the league?** `team_count(df)` returns the number of different teams.
2. **Which Celtics average over 15 points?** `celtics_scorers(df)` returns a DataFrame of every player whose Team is BOS and whose PTS is over 15.
3. **Who are the league's rising stars?** `rising_stars(df)` adds a PRA column (PTS + REB + AST), then returns a DataFrame of every player under 23 with a PRA over 25.

Questions 2 and 3 return a table (a DataFrame), not a number. Run the file to see your tables.

"Over 15" means more than 15, and "under 23" means 22 or younger. Exact matches don't count.

Every function must work on any table with these columns; the tests also use a small practice table.

## How to run

- See your findings: `python src/hoops_report.py`
- Run the tests: `python -m unittest discover` (or use the "Python Tests" tree in the Testing panel)

## If tests won't run

- **"No module named pandas"**: select the conda/Anaconda interpreter (Cmd/Ctrl+Shift+P → Python: Select Interpreter), then trash the terminal and open a new one.
- If "Python Test Explorer for Visual Studio Code" is installed, uninstall it; it ignores your interpreter choice.
- Open the assignment folder itself (File → Open Folder), not a folder above it.
- Windows: if conda won't activate in the terminal, run `conda init powershell` once in Anaconda Prompt and restart VS Code.
