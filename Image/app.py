import streamlit as st
from openai import OpenAI
import requests
import os 
import uuid
from dotenv import load_dotenv
load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")
client=OpenAI(api_key=api_key)

def generate_image(prompt):
    response=client.images.generate(
        model="dall-e-2",
        prompt=f"{prompt}",
        size="512x512",
        quality="hd",
        n=1,
    )
    return response

st.title("DALL-E-2 Image Generator")
st.markdown("""
            <div style="text-align:center;">
                <h3>This application will help to create an image based on the input prompt</h3>
            </div>
            """,unsafe_allow_html=True)

prompt=st.text_area("Enter your prompt:")

if st.button("Generate Image") and prompt!="":

    st.spinner("Generating Image...")
    image_id=uuid.uuid1()
    response=generate_image(prompt)
    image_data=requests.get(response.data[0].url).content #gettting the image from url
    with open(f"AI_Image/image_{image_id}.png","wb") as f:
        f.write(image_data)
    st.image(response.data[0].url)

