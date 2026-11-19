from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "Online Retail.xlsx"

def load_online_retail(path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """Load the original workbook without changing its contents."""
    df = pd.read_excel(path, sheet_name="Online Retail")
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
    return df
