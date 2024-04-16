import streamlit as st
from openai import OpenAI

f = open('keys/.open_ai_key.txt')
OPENAI_API_KEY = f.read()

client = OpenAI(api_key = OPENAI_API_KEY)

def main():
    st.title("Python Code Review Application")
    
    code_input = st.text_area("Enter your Python code here:")
    
    if st.button("Submit"):
        with st.spinner("Analyzing code..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-16k-0613",
                messages=[
                    {"role": "system", "content":"""You are an Experienced AI assistant that reviews Python code.
                                                    Identify the errors in the code and provide the corrected code"""},
                    {"role": "user", "content": code_input}
                ]
            )   
            st.subheader("Feedback:")
            st.write(response.choices[0].message.content)

if __name__ == "__main__":
    main()