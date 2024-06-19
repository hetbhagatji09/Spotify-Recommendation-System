
import numpy as np
import pandas as pd
import streamlit as st
df=pd.read_csv('spotify.csv')
df=df.iloc[0:20000,:]

def Recommened(artist):
    songs=df[df['artist']==artist]['title'].values
    return songs
st.title('Spotify Data Analysis')

artists=df['artist'].unique()
artist=st.selectbox('spotify',(artists))

if st.button("Recommened"):
    songs=Recommened(artist)
    for i in songs:
        st.text(i)
