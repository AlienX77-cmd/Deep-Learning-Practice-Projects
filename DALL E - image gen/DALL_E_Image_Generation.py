# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 10:59:11 2023

@author: Kittipak
"""

import openai
import urllib.request
import streamlit as st
from PIL import Image


openai.api_key = "Your OpenAI API KEY"

def Generate_Image(image_description):

  img_response = openai.Image.create(
    prompt = image_description,
    n=1,
    size="512x512")
  

  img_url = img_response['data'][0]['url']

  urllib.request.urlretrieve(img_url, 'img.png')

  img = Image.open("img.png")
  
  return img



# Page Title
st.title('DALL.E - Image Generation - OpenAI')

# Text input box for image recognition
img_description = st.text_input('Image Desription')

if st.button('Generate Image'):
    
    generated_img = Generate_Image(img_description)
    st.image(generated_img)