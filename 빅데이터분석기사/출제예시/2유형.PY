# 출력을 원하실 경우 print() 함수 활용
# 예시) print(df.head())

# getcwd(), chdir() 등 작업 폴더 설정 불필요
# 파일 경로 상 내부 드라이브 경로(C: 등) 접근 불가

# 데이터 파일 읽기 예제
import pandas as pd
X_test = pd.read_csv("data/X_test.csv")
X_train = pd.read_csv("data/X_train.csv")
y_train = pd.read_csv("data/y_train.csv")

# 사용자 코딩 
import numpy as np 
import sklearn 
from sklearn.preprocessing import LabelEncoder 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import roc_auc_score 
from xgboost import XGBClassifier 
# Get DF 
X_train_id = X_train.iloc[:, 0] 
X = X_train.iloc[:, 1:] 
X_test_id = X_test.iloc[:, 0] 
X_test = X_test.iloc[:, 1:] 
y = y_train.iloc[:, 1] 
# info # X_train.info() # X_train.isnull().sum() 
# DF preprocessing 
# LabelEncdoder 
X.loc[:, ['주구매상품', '주구매지점']] = X.loc[:, ['주구매상품', '주구매지점']].apply(LabelEncoder().fit_transform) 
X_test.loc[:, ['주구매상품', '주구매지점']] = X_test.loc[:, ['주구매상품', '주구매지점']].apply(LabelEncoder().fit_transform) 
print(X.head())
# NaN to zero 
X.loc[:, ['환불금액']] = X.loc[:, ['환불금액']].fillna(0) 
X_test.loc[:, ['환불금액']] = X_test.loc[:, ['환불금액']].fillna(0) 
# model_selection 
# Model # RFC 
rfc = RandomForestClassifier() 
rfc.fit(X, y) 
pred = rfc.predict_proba(X)[:, 1] 
# Score 
from sklearn.metrics import roc_auc_score 
print(roc_auc_score(y, pred)) 
result_pred = rfc.predict_proba(X_test)[:,1] 
result_pred = pd.DataFrame(result_pred) 
result = pd.concat([X_test_id, result_pred], axis=1) 
result.columns = ['cust_id', 'gender'] 
# print(result) 
y_test_path = '123456.csv' 
result.to_csv(y_test_path, index=False) 
df = pd.read_csv(y_test_path) 
print(df)
# 답안 제출 참고
# 아래 코드 예측변수와 수험번호를 개인별로 변경하여 활용
# pd.DataFrame({'cust_id': X_test.cust_id, 'gender': pred}).to_csv('003000000.csv', index=False)
