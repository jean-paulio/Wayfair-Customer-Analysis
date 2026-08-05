import pandas as pd
import numpy as np

print("Executing RFM Pipeline...")

# 1. Load the ledger
df = pd.read_csv("raw_sales_data.csv")
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['TotalCost'] = df['UnitPrice'] * df['Quantity']

# Set reference date to the day after the last transaction date in simulation
snapshot_date = pd.to_datetime('2026-06-01')

# 2. Group by customer to calculate raw metrics
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days, # Recency
    'InvoiceNo': 'nunique',                                  # Frequency
    'TotalCost': 'sum'                                       # Monetary
}).reset_index()

rfm.columns = ['CustomerID', 'recency', 'frequency', 'monetary']

# 3. Calculate quintile rankings using Pandas qcut (Quantile-based discretization)
# For Recency, smaller values get a higher score (5)
rfm['r_score'] = pd.qcut(rfm['recency'], q=5, labels=[5, 4, 3, 2, 1]).astype(int)
rfm['f_score'] = pd.qcut(rfm['frequency'].rank(method='first'), q=5, labels=[1, 2, 3, 4, 5]).astype(int)
rfm['m_score'] = pd.qcut(rfm['monetary'], q=5, labels=[1, 2, 3, 4, 5]).astype(int)

# 4. Map Segment Names using conditions
def assign_segment(row):
    r, f, m = row['r_score'], row['f_score'], row['m_score']
    if r >= 4 and f >= 4 and m >= 4:
        return 'Champions'
    elif r >= 3 and f >= 3 and m >= 3:
        return 'Loyal Customers'
    elif r >= 3 and f <= 2:
        return 'Promising / New'
    elif r <= 2 and f >= 3:
        return 'At Risk / Can\'t Lose Them'
    elif r <= 2 and f <= 2:
        return 'Hibernating / Lost'
    else:
        return 'About to Sleep / Average'

rfm['customer_segment'] = rfm.apply(assign_segment, axis=1)

# 5. Output to a distinct file
rfm.to_csv("rfm_segments.csv", index=False)
print("Successfully executed calculations!")
print("Output file 'rfm_segments.csv' generated with data science schema.")
