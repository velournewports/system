import streamlit as st
import os
import sys
import cv2
import numpy as np
from PIL import Image
import os.path
import random
import webbrowser

imgExtension = ["jpeg","jpg","png"]
allImages = list()

def chooseRandomImage(directory=r"/users/dentonyoung/downloads/system/dropbox/[system]"):
    for img in os.listdir(directory): #Lists all files
        ext = img.split(".")[len(img.split(".")) - 1]
        if (ext in imgExtension):
            allImages.append(img)
    choice = random.randint(0, len(allImages) - 1)
    chosenImage = allImages[choice] #Do Whatever you want with the image file
    return chosenImage

xp2 = os.path.abspath(r"/users/dentonyoung/downloads/system/dropbox/[system]")
xp3 = xp2+"/"+chooseRandomImage()

st.set_page_config(layout="wide")

url = 'https://www.dropbox.com/home/%5Bsystem%5D'

col1, col2, col3 = st.columns(3)

with col1:
    pass
with col2:
    if st.button('to be incorporated into the [system] click here.'):
        webbrowser.open_new_tab(url)
with col3:
    pass


slot = st.empty()

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

while True:
	chooseRandomImage()
	xp3 = xp2+"/"+chooseRandomImage()
	img = cv2.imread(xp3)
	RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	slot.image(RGB_img)
	cv2.waitKey(10)
	
