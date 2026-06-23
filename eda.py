import pandas as pd
df = pd.read_csv('processed_transactions.csv')
print(df.head())
print(df['Is Laundering'].value_counts())
laundering_df = df[df['Is Laundering']==1]
print(laundering_df)
print(laundering_df['Payment Format'].value_counts())
print(laundering_df['Payment Currency'].value_counts())
print(df['Severity'].value_counts())