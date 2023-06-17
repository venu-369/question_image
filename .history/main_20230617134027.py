import streamlit as st

st.title("Ask a question to an image")

st.header("please uplaod an image")

file = st.file_uploader("", types=["jpeg", "png", "jpg"])

if file:
    # display image
    st.image(file, use_column_width=True)

    # text input
    user_question = st.text_input("Ask a question about your image:")

    # write agent response
    if user_question and user_question != "":
        st.write("dummy response")
