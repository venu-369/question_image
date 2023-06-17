import streamlit as st
from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.chain.conversation.memory import ConversationBufferWindowMemory

from tools import ImageCaptionTool, ObjectDetectionTool


tools = [ImageCaptionTool, ObjectDetectionTool]

conversational_memory = ConversationBufferWindowMemory(
    memory_key = 'chat_history',
    k = 5,
    return_messages = True
)

llm = ChatOpenAI(
    openai_api_key = None,
    temperature=0.3,
    model_name = "gpt-3.5-turbo"
)

agent = initialize_agent(
    agent = "chat-converesational-react-description",
    tools = tools,
    llm = llm,
    max_iterations = 5,
    verbose = True,
    memory=conversational_memory,
    early_stoppy_method = 'generate'
)

st.title("Ask a question to an image")

st.header("please uplaod an image")

file = st.file_uploader("Choose an image", type=["jpeg", "png", "jpg"])

if file:
    # display image
    st.image(file, use_column_width=True)

    # text input
    user_question = st.text_input("Ask a question about your image:")

    # write agent response
    if user_question and user_question != "":
        st.write("dummy response")
