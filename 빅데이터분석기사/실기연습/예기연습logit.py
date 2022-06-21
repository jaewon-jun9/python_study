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
X_train['환불금액']=X_train['환불금액'].fillna(0)
X_test['환불금액']=X_test['환불금액'].fillna(0)
X_test_cust_id=X_test['cust_id']
X_train=X_train.drop(columns=['cust_id'])
X_test=X_test.drop(columns=['cust_id'])
y_train=y_train.drop(columns=['cust_id'])
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
X_train['주구매상품']=encoder.fit_transform(X_train['주구매상품'])
X_train['주구매지점']=encoder.fit_transform(X_train['주구매지점'])
X_test['주구매상품']=encoder.fit_transform(X_test['주구매상품'])
X_test['주구매지점']=encoder.fit_transform(X_test['주구매지점'])
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = pd.DataFrame(scaler.fit_transform(X_train), columns= X_train.columns)
X_test = pd.DataFrame(scaler.fit_transform(X_test), columns= X_test.columns)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train,y_train)
y_test_pre=model.predict(X_test)
y_test_pre=pd.DataFrame(y_test_pre)
final = pd.concat([X_test_cust_id,y_test_pre],axis=1).rename(columns={0:'gender'})
print(final)
final.to_csv('12345.csv', index=False)
res2=pd.read_csv('12345.csv')
 # 답안 제출 참고
 # 아래 코드 예측변수와 수험번호를 개인별로 변경하여 활용
pd.DataFrame({'cust_id': X_test_cust_id, 'gender': model.predict(X_test)}).to_csv('003000000.csv', index=False)
res=pd.read_csv('003000000.csv')
print(res)
print(res2)
