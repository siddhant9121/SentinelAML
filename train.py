import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import IsolationForest 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import joblib
df = pd.read_csv('processed_transactions.csv')
x =df[['From Bank','Payment Currency','Payment Format','To Bank','Amount Received','Amount Paid']]
y = df['Is Laundering']
le =LabelEncoder()
x['Payment Format'] = le.fit_transform(x['Payment Format'])
le =LabelEncoder()
x['Payment Currency']= le.fit_transform(x['Payment Currency'])
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state= 42)
model = RandomForestClassifier()
sm = SMOTE (random_state=42)
x_train,y_train = sm.fit_resample(x_train, y_train)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print (classification_report(y_test, y_pred))
joblib.dump(model, 'aml_model.pkl')