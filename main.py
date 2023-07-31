import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI

# export OPENAI_API_KEY="..."  # first export your api key
template = """
    Below is an email that may be poorly worded.
    Your goal is to :
    - Properly format the email
    - Convert the input email to a specified tone
    - Convert the input email to a specified language email
    
    Here are some example different Tones:
    - Formal: We went to Barcelona for the weekend.we have a lot of things to tell you
    - Informal: Went to Barcelona for the weekend,Lots to tell you.
    
    Here are some examples of words in different dialects:
    - American English: French Fries, cotton candy, apartment, garbage, cookie
    - British English:chips,candyfloss,flag, rubbish, biscuit
    Below is the email, tone and language
    Tone:{tone}
    LANGUAGE :{dialect}
    EMAIL:{email}
    
    YOUR RESPONSE:
"""
prompt = PromptTemplate(input_variables=["tone", "dialect", "email"], template=template)


def load_llm():
    llm = OpenAI(temperature=.5)
    return llm


llm = load_llm()
# 设置网页title
st.set_page_config(page_title="Generate Good Email", page_icon=":robot:")
st.header("Globalize Text")

st.markdown("Often professionals would like to improve their emails, but don't have the skill to do so.\n\n"
            "This tool will help you improve you email skills by converting your emails into a more professional "
            "format,"
            " This tools is powered by [LangChain](https://www.langchain.com) and [OpenAl](https://openai.com/)")

st.markdown("### Enter Your Email To Convert")


def get_text():
    input_text = st.text_area(label="", placeholder="Your Email...", key="email_input", height=200, )
    return input_text


col1, col2 = st.columns(2)
with col1:
    option_tone = st.selectbox(label="Which tone would you like your email to have?", options=("Formal", "Informal"))

with col2:
    option_dialect = st.selectbox(label="Which dialect would you like?",
                                  options=("American English", 'British English'))
email_text = get_text()

st.markdown("### Your Converted Email:")
if email_text:
    prompt_email = prompt.format(tone=option_tone, dialect=option_dialect, email=email_text)
    response = llm(prompt_email)
    st.write(response)
