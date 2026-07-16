
import streamlit as st

st.sidebar.title('사이드바 타이틀')
page = st.sidebar.radio( '페이지선택', ['홈','소개','설정'])

if page=='홈':
    st.title('🏠 홈')
    st.write('여기는 홈과 관련있는 페이지를')
elif page=="소개":
    st.title('ℹ️ 소개')
    st.write('여기는 소개 관련있는 페이지를')
elif page=="설정":
    st.title("⚙️ 설정")
    st.write('여기는 설정 관련있는 페이지를')
