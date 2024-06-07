#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import streamlit.components.v1 as components
import os

# Set the path to the HTML file
html_file_path = '/Users/eliasgomez/Desktop/qgis2web_2024_06_07-12_54_19_628430/index.html'

# Function to load HTML file
def load_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_data = file.read()
    return html_data

# Load HTML data
html_data = load_html(html_file_path)

# Display the HTML in Streamlit
components.html(html_data, height=600, scrolling=True)

# Run the Streamlit app using: streamlit run your_script.py

