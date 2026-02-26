# import gradio as gr
# from main import generate_course, save_html
#
# def run(topic):
#     result = generate_course(topic)
#     save_html(result)
#     return result
#
# demo = gr.Interface(
#     fn=run,
#     inputs="text",
#     outputs="text",
#     title="AI课程生成器"
# )
#
# demo.launch(share=True)

import streamlit as st
from main import generate_course

st.title("AI课程生成器")

topic = st.text_input("输入课程名")

if st.button("运行"):
    result = generate_course(topic)
    st.write(result)