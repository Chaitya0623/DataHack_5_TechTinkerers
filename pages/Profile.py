import streamlit as st
import time
import numpy as np
import datetime

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)
project_list = []
if 'project_list' not in st.session_state:
        st.session_state.project_list = []

with st.container():
    project_name = st.text_input('Project Name')
    description = st.text_area('Description')
    link = st.text_input('Link')
    start_date = st.date_input('Start Date', datetime.date.today())

    # Button to add project to the list
    if st.button('Add'):
        project = {
            'Project Name': project_name,
            'Description': description,
            'Start Date': start_date,
            'Link': link
        }
        st.session_state.project_list.append(project)


   # Create a global list to store project details
  
    # Create a container to group input fields and project list
  
# Display the list of projects
st.header('List of Projects')
col1, col2 = st.columns(2)

for idx, project in enumerate(st.session_state.project_list):
    background_color = '#90EE90' if idx % 2 == 0 else '#FFD700'

    with (col1 if idx % 2 == 0 else col2):
        st.subheader(f'Project #{idx + 1}')
        st.write(f'**Project Name:** {project["Project Name"]}')
        st.write(f'**Description:** {project["Description"]}')
        st.write(f'**Start Date:** {project["Start Date"]}')
        st.write(f'**Link:** [{project["Link"]}]({project["Link"]})')