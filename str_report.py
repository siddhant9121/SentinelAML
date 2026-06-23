import pandas as pd
from datetime import datetime
df =pd.read_csv('flagged_transactions.csv')
def assign_severity(row):
    if row['Payment Format'] == 'Bitcoin' or row['Payment Format'] == 'Cash':
        return 'High'
    elif row['Amount Paid']> 10000:
        return 'Medium'
    else:
        return 'Low'
df['Severity']= df.apply(assign_severity, axis =1)
print(df['Severity'].value_counts())
with open('STR_Report.txt','w') as f:
    f.write("SUSPICIOUS TRANSACTION REPORT\n")
    f.write(df['Severity'].value_counts().to_string())
    f.write(f"Total Flagged Transactions: {len(df)}\n")

    