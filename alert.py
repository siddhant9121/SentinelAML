import pandas as pd 
from sklearn.preprocessing import LabelEncoder
import joblib
model =joblib.load('aml_model.pkl')
df = pd.read_csv('processed_transactions.csv')
x =df[['From Bank','Payment Currency','Payment Format','To Bank','Amount Received','Amount Paid','Is_Round_Amount','Is_Cross_Currency']]
le = LabelEncoder()
x['Payment Format'] = le.fit_transform(x['Payment Format'])
le =LabelEncoder()
x['Payment Currency']= le.fit_transform(x['Payment Currency'])
y_prob = model.predict_proba(x)[:, 1]
y_pred = (y_prob >= 0.05).astype(int)
df['Predicted'] = y_pred
def assign_severity(row):
    if row['Payment Format'] == 'Bitcoin' or row['Payment Format'] == 'Cash':
        return 'High'
    elif row['Amount Paid']> 10000:
        return 'Medium'
    else:
        return 'Low'
df['Severity'] = df.apply(assign_severity, axis=1)
alerts = df[(df['Predicted'] == 1) & (df['Severity'] != 'Low')]
print (alerts)
print(f"Total alerts: {len(alerts)}")