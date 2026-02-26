import streamlit as st
from main import generate_course

st.title("📚 AI课程生成器")

topic = st.text_input("请输入课程主题", "具身智能")

if st.button("生成课程"):
    with st.spinner("生成中..."):
        result = generate_course(topic)
        st.text_area("课程内容", result, height=600)