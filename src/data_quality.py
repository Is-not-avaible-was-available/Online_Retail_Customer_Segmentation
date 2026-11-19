import pandas as pd

def missing_value_summary(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        "data_type": df.dtypes.astype(str),
        "missing_count": df.isna().sum(),
        "missing_pct": (df.isna().mean() * 100).round(2),
        "unique_nonmissing": df.nunique(dropna=True),
    }).rename_axis("variable").reset_index()

def core_quality_metrics(df: pd.DataFrame) -> pd.Series:
    invoice_text = df["InvoiceNo"].astype("string")
    is_cancel = invoice_text.str.startswith("C", na=False)
    return pd.Series({
        "observations": len(df),
        "variables": df.shape[1],
        "exact_duplicate_excess_rows": int(df.duplicated().sum()),
        "unique_customers_nonmissing": int(df["CustomerID"].nunique()),
        "unique_invoices": int(df["InvoiceNo"].nunique()),
        "unique_products": int(df["StockCode"].nunique()),
        "countries": int(df["Country"].nunique()),
        "c_prefixed_rows": int(is_cancel.sum()),
        "distinct_c_prefixed_invoices": int(df.loc[is_cancel, "InvoiceNo"].nunique()),
        "negative_quantity_rows": int((df["Quantity"] < 0).sum()),
        "zero_unit_price_rows": int((df["UnitPrice"] == 0).sum()),
        "negative_unit_price_rows": int((df["UnitPrice"] < 0).sum()),
        "date_min": df["InvoiceDate"].min(),
        "date_max": df["InvoiceDate"].max(),
    }, name="value")
