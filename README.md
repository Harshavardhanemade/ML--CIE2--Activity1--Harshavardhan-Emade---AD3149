# Machine Learning CIE 2 — Dataset Preparation & Exploratory Data Analysis

**Activity 1:** Dataset Preparation Activity  
**Unit I:** Foundations & Data Preparation  
**Student:** Harshavardhan Emade  
**Roll Number:** AD3149  
**Branch:** AI & DS  
**Target level:** Second Year Engineering — Machine Learning Laboratory

## 1. Project objective
Build a reproducible, beginner-friendly data preparation pipeline using Python on a public tabular dataset. The workflow includes data ingestion, structural inspection, missing-value treatment, duplicate removal, categorical consistency, EDA, one-hot encoding, numerical standardization, validation and export.

**Scope boundary:** No prediction model is trained or evaluated.

## 2. Dataset and public source
- Dataset: Titanic Passenger Survival Dataset
- Source: https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv
- Direct CSV: https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv
- Format: CSV
- Common source dimensions: 891 rows × 15 columns. The notebook prints the actual dimensions read at runtime.

### Data dictionary

| Column | Type / nature | Description |
|---|---|---|
| survived | Integer / binary target | 0 = did not survive; 1 = survived |
| pclass | Integer / ordinal | Ticket class: 1, 2, 3 |
| sex | Text / nominal | Passenger sex category |
| age | Numeric / continuous | Age in years; contains missing values |
| sibsp | Integer / discrete | Siblings and spouses aboard |
| parch | Integer / discrete | Parents and children aboard |
| fare | Numeric / continuous | Ticket fare |
| embarked | Text / nominal | Port code: C, Q, or S |
| class | Text / redundant | Text label for pclass |
| who | Text / nominal | man, woman, or child |
| adult_male | Boolean / binary | Adult male indicator |
| deck | Text / sparse | Cabin deck; highly incomplete |
| embark_town | Text / redundant | Text label for embarked |
| alive | Text / redundant | Text label for survived |
| alone | Boolean / binary | Whether passenger travelled without family |

## 3. Technology stack
- Python 3
- pandas, NumPy
- Matplotlib, Seaborn
- scikit-learn (`StandardScaler`)
- Jupyter Notebook / Google Colab

## 4. Project structure

```text
ML-CIE2-Harshavardhan-AD3149/
├── dataset_preparation.ipynb
├── README.md
├── requirements.txt
├── build_notebook.py
├── prepared_titanic.csv          # generated when notebook is run
└── reports/
    ├── Activity_Report.pdf
    └── figures/
        ├── age_distribution.png   # generated when notebook is run
        ├── survival_counts.png    # generated when notebook is run
        └── age_vs_fare.png        # generated when notebook is run
```

## 5. Running the notebook

### Option A — Google Colab
1. Open https://colab.research.google.com/
2. Upload `dataset_preparation.ipynb`.
3. Select **Runtime → Run all**.
4. The notebook downloads the public Titanic CSV and generates the prepared CSV and EDA figures.

### Option B — Local Jupyter / VS Code
```bash
git clone https://github.com/harshavardhanemade/ML-CIE2-Dataset-Preparation-22.git
cd ML-CIE2-Dataset-Preparation-22
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook dataset_preparation.ipynb
```
Run cells sequentially from top to bottom. Internet access is required for the first dataset download.

## 6. Data cleaning methodology
- **deck:** removed because it is highly sparse; imputing most entries would create substantial synthetic information.
- **age:** missing values replaced with the median, a statistic less sensitive to extreme values than the mean.
- **embarked:** missing values replaced with the mode because it is categorical.
- **Duplicates:** exact duplicates are removed after dropping `deck`. Therefore, the duplicate count is defined on the remaining columns and is printed dynamically by the notebook.
- **Text consistency:** surrounding whitespace is stripped from object columns.
- **Redundant fields:** `alive`, `class`, and `embark_town` are dropped because they duplicate `survived`, `pclass`, and `embarked`.

### Data leakage note
For a real predictive workflow, imputation and scaling parameters should be fitted on training data only, then applied to validation/test data. This activity prepares the full dataset for demonstration and does not claim to be a leakage-safe modelling pipeline.

## 7. Exploratory Data Analysis
The notebook creates and saves three 300-DPI figures:
1. `age_distribution.png` — passenger age histogram with KDE and median indicator.
2. `survival_counts.png` — count plot for survived and not-survived classes.
3. `age_vs_fare.png` — age-versus-fare scatter plot, distinguished by survival status.

Interpretations should be drawn from the executed plots. Correlation or association must not be described as proof of causation.

## 8. Encoding and scaling
- Boolean fields `adult_male` and `alone` are converted to 0/1.
- `pclass` remains an ordinal integer.
- Nominal fields `sex`, `embarked`, and `who` are one-hot encoded using `pandas.get_dummies(..., drop_first=True)`.
- Continuous features `age` and `fare` are standardized using scikit-learn `StandardScaler`.
- Target `survived`, ordinal class, family counts and binary indicators are not scaled.

## 9. Validation and output
The notebook asserts that:
- no missing cells remain,
- no duplicate rows remain,
- the `survived` target column is retained,
- the target contains only binary values.

It then exports `prepared_titanic.csv` and prints the raw/prepared dimensions, duplicate count and validation results. Counts and final dimensions are intentionally calculated at runtime rather than copied as fixed claims.

## 10. Evaluation checklist mapping

| Evaluation criterion | Evidence |
|---|---|
| Dataset selection and understanding | Public source URL, shape inspection and data dictionary |
| Missing values and data quality | Missing-value audit, median/mode imputation, sparse-column removal, duplicate handling |
| EDA and visualisations | Three saved plots using Matplotlib and Seaborn |
| Encoding and scaling | One-hot encoding with reference category dropped; StandardScaler on continuous fields |
| Prepared dataset and conclusion | Assertions, CSV export and clear scope statement |

## 11. GitHub publishing
Suggested public repository URL:
https://github.com/harshavardhanemade/ML-CIE2-Dataset-Preparation-22

After creating the repository on GitHub, push the project using Git:
```bash
git init
git add .
git commit -m "Add ML CIE 2 dataset preparation and EDA project"
git branch -M main
git remote add origin https://github.com/harshavardhanemade/ML-CIE2-Dataset-Preparation-22.git
git push -u origin main
```

## 12. Acknowledgement
“This project was completed as part of the Machine Learning CIE 2 activity. Faculty reference and Machine Learning learning resources: https://github.com/Princy2129”

**Academic integrity note:** Verify notebook outputs after execution and follow your faculty's submission format. Do not report fixed counts or dimensions unless they match your actual run.
