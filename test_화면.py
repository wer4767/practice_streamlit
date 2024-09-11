import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 가상의 RPA 작업 데이터 생성
data = {
    'Task': ['Task A', 'Task B', 'Task C', 'Task D'],
    'Status': ['Completed', 'Failed', 'Completed', 'In Progress'],
    'Processed Items': [150, 80, 120, 50],
    'Processing Time (min)': [10, 15, 12, 8]
}

df = pd.DataFrame(data)

# 제목 설정
st.title("RPA 시스템 대시보드")

# 작업 상태를 표시하는 테이블
st.header("작업 현황")
st.dataframe(df)

# 처리된 작업 수를 막대 그래프로 시각화
st.header("처리된 작업 수")
fig, ax = plt.subplots()
ax.bar(df['Task'], df['Processed Items'], color='skyblue')
ax.set_xlabel('작업')
ax.set_ylabel('처리된 작업 수')
ax.set_title('작업별 처리된 작업 수')
st.pyplot(fig)

# 처리 시간 평균을 원형 그래프로 시각화
st.header("처리 시간")
fig, ax = plt.subplots()
labels = df['Task']
sizes = df['Processing Time (min)']
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
ax.set_title('작업별 처리 시간 분포')
st.pyplot(fig)

# 필터를 통해 상태별 작업 현황 필터링
st.header("상태별 작업 현황")
status_filter = st.selectbox("상태 선택", ["All"] + list(df['Status'].unique()))
if status_filter != "All":
    filtered_df = df[df['Status'] == status_filter]
else:
    filtered_df = df
st.dataframe(filtered_df)
