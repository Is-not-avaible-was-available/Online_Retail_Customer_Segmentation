# Online Retail Customer Segmentation

Course project: Introduction to Machine Learning — MS Analytics

## Project structure

```text
Online_Retail_Customer_Segmentation/
├── data/
│   ├── raw/                 # Original workbook — do not edit
│   ├── interim/             # Temporary analysis extracts
│   └── processed/           # Validated datasets for later modelling
├── notebooks/
│   ├── 01_dataset_understanding.ipynb
│   ├── 02_data_quality_assessment.ipynb
│   └── 03_exploratory_data_analysis.ipynb
├── src/                     # Reusable Python functions
├── reports/phase_2/
│   ├── figures/
│   ├── tables/
│   └── (final report will be saved here)
├── outputs/                 # Logs and supplementary outputs
├── requirements.txt
└── README.md
```

## Setup (Windows + VS Code)

1. Extract this project folder to a convenient location.
2. Open the folder `Online_Retail_Customer_Segmentation` in VS Code.
3. Open Terminal → New Terminal.
4. Create a virtual environment:

   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use Command Prompt:

   ```cmd
   .venv\Scripts\activate.bat
   ```

5. Install dependencies:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

6. Register the notebook kernel:

   ```powershell
   python -m ipykernel install --user --name online-retail-ml --display-name "Python (Online Retail ML)"
   ```

7. Open the `notebooks` folder and run notebooks in numerical order. Select the
   `Python (Online Retail ML)` kernel when prompted.

## Data source

UCI Machine Learning Repository — Online Retail:
https://archive.ics.uci.edu/dataset/352/online+retail

The original workbook is included at `data/raw/Online Retail.xlsx`. Do not overwrite
or manually edit this file. All analysis should read from this raw source and write
derived outputs to the designated folders.

## Phase 2 decisions currently agreed

- Preserve and audit the original 541,909-row workbook before modifications.
- CustomerID is an aggregation key, not a numeric clustering feature.
- Country is reserved for post-cluster profiling in the planned modelling workflow.
- Option A: cancellation/return records are excluded from primary RFM purchase
  calculations and described separately.
- Exact duplicate rows must be quantified and investigated. The primary analytical
  copy may remove exact duplicates, with a sensitivity check retaining them.
- Do not delete extreme values automatically.
- Missing CustomerID records remain in the raw audit but cannot be assigned to a
  customer-level cluster.

These are project decisions to test and document; the notebooks should report the
actual values computed from the workbook rather than hard-code expected results.

## Reproducibility

Run all three notebooks from top to bottom in order. Do not run cells selectively
unless you understand their dependencies. The notebooks write tables and figures
under `reports/phase_2/` and temporary derived data under `data/interim/`.
