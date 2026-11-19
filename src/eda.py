import pandas as pd

def customer_identified_paid_view(df: pd.DataFrame, remove_exact_duplicates: bool = True) -> pd.DataFrame:
    """Descriptive paid-purchase view; does not mutate the original DataFrame.

    Rules: positive Quantity, positive UnitPrice, non-C-prefixed invoice,
    and non-missing CustomerID. Exact duplicates can optionally be removed.
    """
    invoice_text = df["InvoiceNo"].astype("string")
    is_cancel = invoice_text.str.startswith("C", na=False)
    mask = (
        (df["Quantity"] > 0)
        & (df["UnitPrice"] > 0)
        & (~is_cancel)
        & (df["CustomerID"].notna())
    )
    view = df.loc[mask].copy()
    if remove_exact_duplicates:
        view = view.drop_duplicates().copy()
    view["LineValue"] = view["Quantity"] * view["UnitPrice"]
    view["Month"] = view["InvoiceDate"].dt.to_period("M").astype(str)
    return view
