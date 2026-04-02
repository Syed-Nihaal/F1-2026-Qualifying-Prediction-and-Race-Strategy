# F1 2026 Qualifying Prediction and Race Strategy

This repository contains race-weekend analysis notebooks for the 2026 Formula 1 season.  
Each round notebook builds a data pipeline from FastF1 session data, cleans lap-level datasets, trains qualifying and race-related models, and exports reusable CSV outputs.

## Scope

- Round 1: Australian GP 2026
- Round 2: Chinese GP 2026
- Round 3: Japanese GP 2026
- ~~Round 4: Bahrain GP 2026~~
- ~~Round 5: Saudi Arabian GP 2026~~
- Round 4: Miami GP 2026
- Round 5: Canadian GP 2026
- Round 6: Monaco GP 2026
- Round 7: Barcelona-Catalunya GP 2026
- Round 8: Austrian GP 2026
- Round 9: British GP 2026
- Round 10: Belgian GP 2026
- Round 11: Hungarian GP 2026
- Round 12: Dutch GP 2026
- Round 13: Italian GP 2026
- Round 14: Spanish GP 2026
- Round 15: Azerbaijan GP 2026
- Round 16: Singapore GP 2026
- Round 17: United States GP 2026
- Round 18: Mexico City GP 2026
- Round 19: Sao Paulo GP 2026
- Round 20: Las Vegas GP 2026
- Round 21: Qatar GP 2026
- Round 22: Abu Dhabi GP 2026

## Workflow

The same workflow pattern is used in each round folder:

1. Load session data from FastF1
2. Cache downloaded timing/session data locally
3. Build combined and cleaned lap-level datasets
4. Prepare top-team subsets
5. Run qualifying/race strategy modeling and visualization

## Repository Structure

```text
.
|-- readme.md
|-- Round_1_Australian_GP_2026/
|   |-- F1_2026_Australian_GP_Qualifying_and_Race_Strategy.ipynb
|   |-- f1_2026_australian_gp_combined_laps.csv
|   |-- f1_2026_australian_gp_cleaned_laps.csv
|   |-- f1_2026_australian_gp_qualifying_laps.csv
|   |-- f1_2026_australian_gp_qualifying_cleaned_laps.csv
|   |-- f1_2026_australian_gp_top_teams_laps.csv
|   |-- f1_2026_australian_gp_qualifying_top_teams_laps.csv
|-- Round_2_Chinese_GP_2026/
|   |-- F1_2026_Chinese_GP_Qualifying_and_Race_Strategy.ipynb
|   |-- f1_2026_chinese_gp_combined_laps.csv
|   |-- f1_2026_chinese_gp_cleaned_laps.csv
|   |-- f1_2026_chinese_gp_qualifying_laps.csv
|   |-- f1_2026_chinese_gp_qualifying_cleaned_laps.csv
|   |-- f1_2026_chinese_gp_top_teams_laps.csv
|   |-- f1_2026_chinese_gp_qualifying_top_teams_laps.csv
`-- Round_3_Japanese_GP_2026/
    |-- F1_2026_Japanese_GP_Qualifying_and_Race_Strategy.ipynb
    |-- f1_2026_japanese_gp_combined_laps.csv
    |-- f1_2026_japanese_gp_cleaned_laps.csv
    |-- f1_2026_japanese_gp_qualifying_laps.csv
    |-- f1_2026_japanese_gp_qualifying_cleaned_laps.csv
    |-- f1_2026_japanese_gp_top_teams_laps.csv
    |-- f1_2026_japanese_gp_qualifying_top_teams_laps.csv
```

## Requirements

- Python 3.10+
- Jupyter Notebook or JupyterLab
- Internet access for initial FastF1 data download

Python packages used in the notebooks:

- fastf1
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- xgboost

Install with:

```bash
pip install fastf1 pandas numpy matplotlib seaborn scikit-learn xgboost jupyter
```

## Quick Start

1. Clone or open this repository in VS Code.
2. Open one of the round notebooks.
3. Select a Python environment with the dependencies installed.
4. Run all cells from top to bottom.

Example:

- `Round_1_Australian_GP_2026/F1_2026_Australian_GP_Qualifying_and_Race_Strategy.ipynb`

## Data and Caching Behavior

Each notebook uses FastF1 cache directories inside the corresponding round folder.  
On the first run, session data is downloaded and stored in that cache directory.  
Subsequent runs will reuse cached files for faster execution.

Notes:

- Keep cache folders if you want reproducible reruns without re-downloading.
- Delete a round cache folder if you want a fresh pull of FastF1 data.
- Ensure cache directories exist before enabling cache in code.

## Output Files

Each round generates or updates CSV files, including:

- Combined laps dataset
- Cleaned laps dataset
- Qualifying laps dataset
- Cleaned qualifying laps dataset
- Top teams laps dataset
- Qualifying top teams laps dataset

These outputs are designed to support model training, evaluation, and strategy comparisons across sessions.

## Reproducibility Tips

- Run notebook cells in order to preserve pipeline state.
- Avoid editing generated CSV names unless you update all references.
- Use `import fastf1 as ff1` consistently.
- All notebooks are named `F1_2026_[Round]_Qualifying_and_Race_Strategy.ipynb`.
- All csv files are named `f1_2026_[Round]_[Session]_[Dataset].csv`.

## Disclaimer

This project is for educational and analytical purposes. Predictions and strategy outputs are model-based estimates and should not be treated as official race outcomes.

This project uses data sourced via the FastF1 Python library. FastF1 is an open-source project licensed under the MIT License.

All data sourced is the property of the Formula One World Championship Limited. This project is an independent, non-commercial analysis and is not affiliated with, endorsed by, or otherwise connected to Formula 1, its partners, or its subsidiaries.
