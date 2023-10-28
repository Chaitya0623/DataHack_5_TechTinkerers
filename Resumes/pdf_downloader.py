import pandas as pd
import requests
import os

# Load the resumes.csv file
df = pd.read_csv('resumes.csv')

# Create a new dataframe with columns containing the word "Resume"
resume_df = pd.DataFrame()
for col in df.columns:
    if 'Resume' in col:
        resume_df[col] = df[col]

# Create Resumes folder if it doesn't exist
if not os.path.exists('Resumes'):
    os.makedirs('Resumes')

# Download and save pdfs
for col in resume_df.columns:
    for link in resume_df[col]:
        if type(link)==str:
            response = requests.get(link)
            filename = link.split('/')[-1]
            with open(f'Resumes/{filename}', 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {filename}")            