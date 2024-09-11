import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from streamlit_option_menu import option_menu




# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # 윈도우에서 사용하는 경우
# plt.rcParams['font.family'] = 'AppleGothic'  # Mac에서 사용하는 경우
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지
# 데이터베이스 연결 설정
DB_TYPE = 'mysql+pymysql'  # MySQL의 경우
DB_HOST = '172.18.30.14'
DB_PORT = '3306'
DB_USER = user='ddm2'
DB_PASSWORD = 'chainhan12!'
DB_NAME = db='rpa_system'


# SQLAlchemy 연결 설정
engine = create_engine(f"{DB_TYPE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# SQL 쿼리로 데이터 불러오기
query = "SELECT company as 회사, dept as 부서, position as 직위, name as 이름 FROM rpa_history"
df = pd.read_sql(query, engine)

# Streamlit 대시보드
st.title("RPA 시스템 데이터 분석 대시보드")

# 데이터 미리보기
st.subheader("데이터 미리보기")
st.write(df.head())

# 데이터 간단한 통계
st.subheader("데이터 통계")
st.write(df.describe())

# 선택한 열의 값에 따른 막대 그래프
# st.sidebar.header("분석 설정")
# column = st.sidebar.selectbox("분석할 열 선택", df.columns)

st.sidebar.header("분석 설정")
column = st.sidebar.selectbox("분석할 열 선택", df.columns)
with st.sidebar:
    choice = option_menu("Menu", ["페이지1", "페이지2", "페이지3"],
                         icons=['house', 'kanban', 'bi bi-robot'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "4!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
        "nav-link-selected": {"background-color": "#08c7b4"},
    }
    )


# 선택한 열의 데이터 시각화
st.subheader(f"{column} 값 분포")
fig, ax = plt.subplots()
ax.hist(df[column].dropna(), bins=20, color="skyblue", edgecolor="black")
st.pyplot(fig)

# 데이터 다운로드 기능
csv = df.to_csv(index=False).encode('utf-8')
st.sidebar.download_button(label="CSV 다운로드", data=csv, file_name='data.csv', mime='text/csv')
