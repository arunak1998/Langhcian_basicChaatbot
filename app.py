from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


import streamlit as st

import os
from dotenv import load_dotenv


os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")
##Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


##### Prompt Template

prompt=ChatPromptTemplate.from_messages(

    [
       ( "system","You are a helpful assistance .Please respond to the queries"),
       ("user","Question: {question}")

    ]
)


##Streamlit

st.title("Lanchain Chatbot with Gemini API")
input_text=st.text_input("Search the Topic U want")


### LLM -Gemini

model=ChatGoogleGenerativeAI(model='gemini-pro',verbose=True,convert_system_message_to_human=True)
output_parser=StrOutputParser()
chain=( prompt| model| output_parser)
print(chain.input_schema.schema())
if input_text:
    st.write(chain.invoke({'question' : input_text}))