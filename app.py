import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch
import streamlit as st

# Load the CSV data
df = pd.read_csv("D:/FData/Community Shield/Man City_vs_Man Utd_EventData.csv")

# Define the plot function
def plot_pass(ax, team_name):
    pass_df = df[(df['type'] == 'Pass') & (df['teamName'] == team_name)]
    pitch = Pitch(pitch_type='uefa')
    pitch.draw(ax=ax)
    pitch.lines(pass_df.x, pass_df.y, pass_df.endX, pass_df.endY, lw=1, ax=ax)

# Streamlit App
st.title("Soccer Match Pass Visualization")

# Select team name
team_name = st.selectbox('Select a team', df['teamName'].unique())

# Plot
fig, ax = plt.subplots()
plot_pass(ax, team_name)

# Display the plot in Streamlit
st.pyplot(fig)