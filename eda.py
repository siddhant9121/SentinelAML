import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('processed_transactions.csv')
print(df.head())
df['Is Laundering'].value_counts().plot(kind='bar')
plt.title('Laundering vs Legitimate')
plt.xlabel('Transaction Type')
plt.ylabel('Count(in million)'), plt.show()
laundering_df = df[df['Is Laundering']==1]
laundering_df['Payment Format'].value_counts().plot(kind ='bar')
plt.xlabel('Payment method')
plt.ylabel('count')
plt.title('Payment Methods vs Laundering')
plt.show()
