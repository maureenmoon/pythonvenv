import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
import streamlit as st

st.title('lemon sales predictor')

lemon = pd.read_csv('data/lemonade01.csv') #dataframe 가져옴

#data preprocessing
X = lemon[['온도']] 
y = lemon['판매량']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Model algorithm 생성
model = LinearRegression()

# Model data fit
model.fit(X_train,y_train)

# Model prediction
y_pred = model.predict(X_test)
st.text(y_pred)

input_temp = st.number_input('input temp to predict',min_value=20, max_value=50, step=1)
if st.button('selling qty predictor'):
    pred = model.predict([[input_temp]])
    st.success(f'estimated selling qty : {pred[0]}') #예측치 결과의 첫번째데이터





