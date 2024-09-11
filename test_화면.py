import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# MariaDB 연결 정보 설정
# 아래 항목을 자신의 MariaDB 서버 정보로 변경하세요.
DB_USER = "ddm2"  # MariaDB 사용자 이름
DB_PASSWORD = "chainhan12!"  # MariaDB 비밀번호
DB_HOST = "172.18.30.14"  # MariaDB 서버 IP 주소 (예: '192.168.1.100')
DB_PORT = "3306"  # 기본 MariaDB 포트 (필요 시 다른 포트 입력)
DB_NAME = "rpa_system"  # 연결하려는 데이터베이스 이름

# MariaDB 연결 URL 구성
DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# SQLAlchemy 엔진 생성
engine = create_engine(DB_URL)

# 데이터베이스에서 데이터 불러오기 함수
@st.cache_data
def load_data(query):
    with engine.connect() as connection:
        data = pd.read_sql(query, connection)
    return data

# Streamlit 앱 시작
st.title("MariaDB 데이터 시각화 대시보드")

# 데이터 쿼리 작성
query = "SELECT * FROM rpa_history"  # 원하는 쿼리 작성
data = load_data(query)

# 데이터 표시
if not data.empty:
    st.write("데이터 미리보기:")
    st.dataframe(data)  # 테이블 형태로 데이터 출력
    
    # 데이터 시각화 - 예시로 막대 그래프와 라인 그래프 표시
    st.write("데이터 시각화 (막대 그래프):")
    if 'category_column' in data.columns and 'value_column' in data.columns:
        bar_chart_data = data[['category_column', 'value_column']].set_index('category_column')
        st.bar_chart(bar_chart_data)

    st.write("데이터 시각화 (라인 그래프):")
    if 'date_column' in data.columns and 'value_column' in data.columns:
        line_chart_data = data[['date_column', 'value_column']].set_index('date_column')
        st.line_chart(line_chart_data)
else:
    st.error("데이터를 불러올 수 없습니다.")
