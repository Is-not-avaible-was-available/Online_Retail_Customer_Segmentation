# Phase 3: Data Preprocessing and Feature Engineering

## 1. Dataset preparation
- Original raw dataset preserved unchanged.
- 5,268 exact duplicate records removed from the analytical copy.
- Cancellation invoices (InvoiceNo beginning with C) separated from purchases.
- Records with missing CustomerID excluded from customer-level analysis.
- Only positive Quantity and positive UnitPrice transactions retained.

## 2. Special transaction treatment
- Zero-price transactions excluded from primary paid-purchase features.
- Negative-price accounting adjustments excluded.
- StockCodes POST, DOT and M excluded from primary merchandise features.
- POST retained in a supplementary merchandise-plus-postage dataset.
- Genuine alphanumeric product StockCodes retained.
- Monetary calculated using Quantity multiplied by UnitPrice.

## 3. Customer-level features
Reference date: 10 December 2011.

RFM:
- Recency: days since the customer's last purchase.
- Frequency: number of distinct purchase invoices.
- Monetary: total merchandise expenditure.

Extended features:
- Average Order Value.
- Total Quantity Purchased.
- Product Diversity.
- Purchase Regularity calculated and retained as a supplementary feature.

Purchase Regularity is missing for customers with only one invoice.
It was not imputed and was excluded from primary clustering features.

## 4. Transformations and outliers
- Log1p applied to Frequency, Monetary, Average Order Value,
  Total Quantity and Product Diversity.
- Recency retained in its original scale before standardisation.
- No blanket removal or capping of statistical outliers.
- Extreme customer transactions investigated individually.

## 5. Matched-reversal sensitivity analysis
Two purchase lines were identified with strongly matching cancellation
records based on customer, product, quantity, unit price and timing.

- Customer 12346: purchase value £77,183.60.
- Customer 16446: purchase value £168,469.60.
- Total matched purchase value: £245,653.20.

Both lines were excluded only from the sensitivity dataset.
The original merchandise dataset was retained as the baseline.

## 6. Feature sets
- RFM: Recency, Frequency, Monetary.
- Extended: RFM plus Average Order Value, Total Quantity,
  Product Diversity.
- Reduced Extended: Extended features excluding Total Quantity.

## 7. Scaling
Both StandardScaler and RobustScaler were applied separately
to all three feature sets.

## 8. Final modelling datasets
- Original customer population: 4,335 customers.
- Sensitivity customer population: 4,334 customers.
- Six scaled original datasets.
- Six scaled sensitivity datasets.
- CustomerID retained in exported files for cluster mapping,
  but excluded from clustering model inputs.

## 9. Limitations and considerations
- Cancellation matching is based on strong transaction-level
  evidence but does not establish the full business context.
- Exact duplicate removal may remove legitimate repeated entries
  because the dataset does not provide a unique transaction-line ID.
- Country is reserved for post-clustering profiling.
- Clustering results will be evaluated using internal metrics,
  cluster profiles and interpretability rather than classification accuracy.