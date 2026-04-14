# F1 2026 Qualifying Prediction and Race Strategy

This repository contains race-weekend analysis notebooks for the 2026 Formula 1 season.
Each round notebook builds a data pipeline from FastF1 session data, cleans lap-level datasets, trains qualifying and race-related models, and exports reusable CSV outputs.

## Schedule

| Round | Event | Dates | Notes |
| --- | --- | --- | --- |
| Testing 1 | Bahrain 2026 | 11 - 13 FEB | Pre-season |
| Testing 2 | Bahrain 2026 | 18 - 20 FEB | Pre-season |
| Round 1 | Australian GP 2026 | 06 - 09 MAR | None |
| Round 2 | Chinese GP 2026 | 13 - 15 MAR | Sprint Weekend |
| Round 3 | Japanese GP 2026 | 27 - 29 MAR | None |
| ~~Round 4~~ | ~~Bahrain GP 2026~~ | ~~10 - 12 APR~~ | Cancelled |
| ~~Round 5~~ | ~~Saudi Arabian GP 2026~~ | ~~17 - 19 APR~~ | Cancelled |
| Round 4 | Miami GP 2026 | 01 - 03 MAY | Sprint Weekend |
| Round 5 | Canadian GP 2026 | 22 - 24 MAY | Sprint Weekend |
| Round 6 | Monaco GP 2026 | 05 - 07 JUN | None |
| Round 7 | Barcelona-Catalunya GP 2026 | 12 - 14 JUN | None |
| Round 8 | Austrian GP 2026 | 26 - 28 JUN | None |
| Round 9 | British GP 2026 | 03 - 05 JUL | Sprint Weekend |
| Round 10 | Belgian GP 2026 | 17 - 19 JUL | None |
| Round 11 | Hungarian GP 2026 | 24 - 26 JUL | None |
| Round 12 | Dutch GP 2026 | 21 - 23 AUG | Sprint Weekend |
| Round 13 | Italian GP 2026 | 04 - 06 SEP | None |
| Round 14 | Spanish GP 2026 | 11 - 13 SEP | None |
| Round 15 | Azerbaijan GP 2026 | 24 - 26 SEP | None |
| Round 16 | Singapore GP 2026 | 09 - 11 OCT | Sprint Weekend |
| Round 17 | United States GP 2026 | 23 - 25 OCT | None |
| Round 18 | Mexico City GP 2026 | 30 - 01 NOV | None |
| Round 19 | Sao Paulo GP 2026 | 06 - 08 NOV | None |
| Round 20 | Las Vegas GP 2026 | 19 - 21 NOV | None |
| Round 21 | Qatar GP 2026 | 27 - 29 NOV | None |
| Round 22 | Abu Dhabi GP 2026 | 04 - 06 DEC | None |

## Workflow

The same workflow pattern is used in each round folder:

1. Load session data from FastF1
2. Cache downloaded timing/session data locally (deleted in the repository due to large file size)
3. Build combined and cleaned lap-level datasets
4. Prepare top-team subsets
5. Run qualifying/race strategy modeling and visualization

## Repository Structure

```text
.
|-- LICENSE
|-- readme.md
|-- Round_1_Australian_GP_2026/
|   |-- F1_2026_Australian_GP_Qualifying_and_Race_Strategy.ipynb
|   |-- f1_2026_australian_gp_combined_laps.csv
|   |-- f1_2026_australian_gp_cleaned_laps.csv
|   |-- f1_2026_australian_gp_qualifying_laps.csv
|   |-- f1_2026_australian_gp_qualifying_cleaned_laps.csv
|-- Round_2_Chinese_GP_2026/
|   |-- F1_2026_Chinese_GP_Qualifying_and_Race_Strategy.ipynb
|   |-- f1_2026_chinese_gp_combined_laps.csv
|   |-- f1_2026_chinese_gp_cleaned_laps.csv
|   |-- f1_2026_chinese_gp_qualifying_laps.csv
|   |-- f1_2026_chinese_gp_qualifying_cleaned_laps.csv
|-- Round_3_Japanese_GP_2026/
|   |-- F1_2026_Japanese_GP_Qualifying_and_Race_Strategy.ipynb
|   |-- f1_2026_japanese_gp_combined_laps.csv
|   |-- f1_2026_japanese_gp_cleaned_laps.csv
|   |-- f1_2026_japanese_gp_qualifying_laps.csv
|   |-- f1_2026_japanese_gp_qualifying_cleaned_laps.csv
`-- Testing_1&2_Bahrain_2026/
    |-- F1_2026_Testing_1&2_Bahrain__Baseline_Benchmarking.ipynb
    |-- f1_2026_testing_1&2_combined_laps.csv
    `-- f1_2026_testing_1&2_cleaned_laps.csv
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

## Cleaning Process

Data cleaning is implemented in `template.py` through a reusable `data_cleaning(data, output_csv_path)` function and is applied to both practice and qualifying lap datasets.

Main steps:

1. Time normalization
    - Converts `LapTime`, `Sector1Time`, `Sector2Time`, and `Sector3Time` into numeric seconds.
    - Handles both already-numeric values and timedelta/string-style values.

2. Deleted lap removal
    - If the `Deleted` column exists, rows flagged as true (`true/1/yes`) are removed.
    - This prevents track-limits or invalidated laps from biasing pace analysis.

3. Inaccurate lap removal
    - If the `IsAccurate` column exists, rows flagged as false (`false/0/no`) are removed.
    - This filters laps with unreliable timing quality.

4. Column pruning
    - Drops high-granularity timing metadata not required for downstream analysis/modeling, such as pit-in/out timestamps, session-time sector columns, deleted-lap metadata, and FastF1-generated flags.

5. Export of cleaned outputs
    - Saves cleaned practice data to `f1_2026_[round]_cleaned_laps.csv`.
    - Saves cleaned qualifying data to `f1_2026_[round]_qualifying_cleaned_laps.csv`.

Result:

- The cleaned tables keep lap-level predictors used in EDA and modeling (`Session`, `Team`, `Driver`, `LapNumber`, `Stint`, `Compound`, `TyreLife`, speed features, and `LapTime`) while removing noisy or non-model inputs.

## Qualifying Modeling Process

Modeling in the notebook is centered on a qualifying-oriented regression pipeline (`qualifying_model_pipeline`) that predicts lap time in seconds.

Target:

- `LapTime`

Data selection and filtering:

1. Start from cleaned all-team practice data.
2. Remove extreme lap-time tails by keeping only the 5th to 95th percentile range.
3. Restrict training rows to `SOFT` compound laps (qualifying-style focus).
4. Drop rows with missing required feature or target values.

Feature engineering approach:

- Numeric base features:
  - `LapNumber`, `TyreLife`, `Stint`
- Optional telemetry/speed features (only if present and numeric):
  - `SpeedST`, `SpeedI1`, `SpeedI2`, `SpeedFL`, `Throttle`, `Brake`, `DRS`
- Categorical features:
  - `Compound`, `Driver`, `Team`, `Session`, `TrackStatus`

Preprocessing and split strategy:

1. Uses `ColumnTransformer`:
    - Numeric columns passed through unchanged.
    - Categorical columns one-hot encoded (`handle_unknown='ignore'`).
2. Uses an 80/20 train-test split (`random_state=324`).
3. Applies session stratification when each session has enough samples.

Baseline and trained models:

- Baseline:
  - `DummyRegressor(strategy='mean')`
- Main regressors (inside full preprocessing pipelines):
  - `RandomForestRegressor`
  - `GradientBoostingRegressor`
  - `XGBRegressor`

Evaluation outputs:

- Global metrics on test set:
  - MAE, RMSE, and R2
- Driver-level diagnostics:
  - Absolute error per driver for each model
  - Best-performing model per driver (`BestModel`, `BestMAE`)

Practical interpretation:

- The pipeline compares model skill against a mean baseline, selects strongest global performance, and also reveals when a different model is better for specific drivers.

### Example Output Interpretation

The notebook prints model comparison tables and driver-level diagnostics. A quick way to read them:

1. Start with the baseline row (`DummyRegressor`)
    - This is the minimum reference level.
    - A useful model should beat baseline on MAE and RMSE, and usually improve R2.

2. Compare global metrics across RF / GB / XGB
    - Lower MAE means smaller average lap-time error (in seconds).
    - Lower RMSE means fewer large misses (more penalty on outliers).
    - Higher R2 means better explained variance in lap times.

3. Read driver-level best model table
    - `BestModel` is selected per driver using lowest validation MAE.
    - `BestMAE` shows practical per-driver prediction quality.
    - It is normal for driver-level best model to differ from the globally best model.

4. Use residual and actual-vs-predicted plots as checks
    - Residuals centered around zero imply lower systematic bias.
    - Tighter residual spread implies more stable behavior across lap contexts.
    - Actual-vs-predicted points close to the diagonal imply stronger calibration.

## Tyre Degradation Model

The notebook includes a second supervised pipeline (`tyredeg_model_pipeline`) focused on degradation-aware lap-time behavior across compounds.

Objective:

- Predict `LapTime` while explicitly learning how pace changes with `TyreLife` and stint context.

Key differences vs qualifying pipeline:

1. Compound scope
    - Keeps all dry compounds (`SOFT`, `MEDIUM`, `HARD`) rather than only SOFT laps.

2. Validation split
    - Uses `GroupShuffleSplit` grouped by `Driver` to reduce driver leakage between train and test.

3. Feature set
    - Numeric core: `LapNumber`, `TyreLife`, `Stint` plus optional speed/telemetry columns when available.
    - Categorical: `Compound`, `Driver`, `Team`, `Session`, `TrackStatus`, and `FreshTyre` when present.

4. Model suite
    - Baseline mean regressor (`DummyRegressor`), plus tuned Random Forest, Gradient Boosting, and XGBoost pipelines.

5. Diagnostics
    - Same MAE/RMSE/R2 framework as qualifying.
    - Driver-level error table (`t_driver_mae`) to identify which model is most reliable per driver.

Practical use:

- This model is used downstream for stint-time projections and strategy scoring, not only standalone accuracy benchmarking.

## Race Strategy Simulation

Race strategy logic in the notebook converts degradation-model predictions into full-race scenario estimates.

Core assumptions and constants:

1. Race length and pit loss
    - `RACE_LAPS = XX`
    - `PIT_STOP_LOSS = 22.0` seconds per stop
    - Warm-up phase handled via `WARM_UP_LAPS = 3`

2. Regulatory/operational constraints
    - At least two compounds must be used.
    - Compound-specific minimum and maximum stint lengths are enforced.

3. Strategy universe generation
    - Builds one-stop and two-stop candidates from pit-window sweeps.
    - Stores each strategy with stint structure, pit laps, and compound order.

Scoring method:

1. Choose best tyre degradation model by validation R2.
2. Build driver-specific context profiles from FP1-FP3 long-run behavior.
3. Predict lap times by compound and tyre life, then compute cumulative stint times.
4. Add pit-stop loss for each stop.
5. Rank all valid strategies by projected total race time.
6. Report primary recommendation per driver/team.

Outputs:

- Driver-by-driver recommended strategy (`Type`, compound sequence, stint lengths, pit laps).
- Predicted total race time in formatted race-time units.

Interpretation note:

- These are deterministic dry-race projections from historical pace/degradation signals; safety cars, incidents, and live track evolution are not explicitly simulated.

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
