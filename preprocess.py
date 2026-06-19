import pandas as pd
import kagglehub
path = kagglehub.dataset_download("ealtman2019/ibm-transactions-for-anti-money-laundering-aml", path = "HI-Small_Trans.csv")
df = pd.read_csv(path)
print(df.columns)
df.rename(columns= {"Account":"Sender_Account", "Account.1": "Receiver_Account"}, inplace = True) 
print(df)
print (df['Is Laundering'].value_counts())
print(df.isnull().sum())
df.to_csv('processed_transactions.csv', index = False)