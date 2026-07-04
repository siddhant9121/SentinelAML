import pandas as pd
import kagglehub

path = kagglehub.dataset_download("ealtman2019/ibm-transactions-for-anti-money-laundering-aml", path="HI-Small_Trans.csv")
df = pd.read_csv(path)

print(df.columns)
df.rename(columns={"Account": "Sender_Account", "Account.1": "Receiver_Account"}, inplace=True)
print(df)
print(df['Is Laundering'].value_counts())
print(df.isnull().sum())
df['Timestamp']= pd.to_datetime(df['Timestamp'])
df = df.set_index('Timestamp')
df=df.sort_index()

df['Is_Round_Amount'] = (df['Amount Paid'] % 1000 == 0).astype(int)
df['Is_Cross_Currency'] = (df['Receiving Currency'] != df['Payment Currency']).astype(int)
df['Sender_Velocity'] = df.groupby('Sender_Account')['Amount Paid'].transform(lambda x: x.rolling('1h').count())

df = df.reset_index()
df.to_csv('processed_transactions.csv', index=False)