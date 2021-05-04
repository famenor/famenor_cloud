import pandas as pd
import numpy as np
from google.oauth2 import service_account
from sklearn.linear_model import LogisticRegression
from datetime import datetime
import pandas_gbq

gamesDF = pd.read_csv('https://github.com/bgweber/Twitch/raw/master/Recommendations/games-expand.csv')
gamesDF['User_ID'] = gamesDF.index
gamesDF['New_User'] = np.floor(np.random.randint(0, 10, gamesDF.shape[0]) / 9)

train = gamesDF[gamesDF['New_User'] == 0]
x_train = train.iloc[:, 0:10]
y_train = train['label']
test = gamesDF[gamesDF['New_User'] == 1]
x_test = test.iloc[:, 0:10]

model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict_proba(x_test)[:, 1]

resultDF = pd.DataFrame({'User_ID': test['User_ID'], 'Pred': y_pred})
resultDF['time'] = str(datetime.now())

table_id = "dsp_demo.user_scores"
project_id = "formal-air-308518"
credentials = service_account.Credentials.from_service_account_file('dsdemo.json')
pandas_gbq.to_gbq(resultDF, table_id, project_id=project_id, if_exists='replace', credentials=credentials)