from dotenv import load_dotenv
load_dotenv()
import streamlit as st 
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title = "Q&A Demo")
st.header("Preethika Gemini LLM Application")
input = st.text_input("Input: ",key = "input")
submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is: ")
    st.write(response)
    
# import google.generativeai as genai

# # Step 1: Set API key
# genai.configure(api_key="AIzaSyB6xqwwRevx7dBj0pRT0eHprtbpbQx4YVY")

# # Step 2: Load model
# model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

# # Step 3: Get response
# response = model.generate_content("Explain black holes in simple terms.")
# print(response.text)

