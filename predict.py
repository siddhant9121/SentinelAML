import pandas as pd 
from sklearn.preprocessing import LabelEncoder
import joblib
model =joblib.load('aml_model.pkl')
df = pd.read_csv('processed_transactions.csv')
x =df[['From Bank','Payment Currency','Payment Format','To Bank','Amount Received','Amount Paid']]
le = LabelEncoder()
x['Payment Currency']= le.fit_transform(x['Payment Currency'])
le = LabelEncoder()
x['Payment Format']= le.fit_transform(x['Payment Format'])
y_pred = model.predict(x)
df['Predicted'] = y_pred
print(df[df['Predicted']==1])
print(f"Total flagged: {len(df[df['Predicted']==1])}")
flagged = df[df['Predicted'] == 1]
flagged.to_csv('flagged_transactions.csv', index = False)