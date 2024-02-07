import streamlit as st
import find_song


def add_files_interface():
    uploaded_song = st.file_uploader("Select song from files", type='MP3', 
                                     accept_multiple_files=False, key=None, 
                                     help=None, on_change=None, args=None, 
                                     kwargs=None, disabled=False, label_visibility="visible")
    if uploaded_song and st.button("Add MP3"):
        return(uploaded_song)
        
    url_input = st.text_input("Enter the URL of the song you want to add")
    if st.button("Add URL") and url_input:
        return(url_input)

def search_song_interface():
    song_to_find = st.file_uploader("Select song from files", type='MP3', 
                                    accept_multiple_files=False, key=None, 
                                    help=None, on_change=None, args=None, 
                                    kwargs=None, disabled=False, label_visibility="visible")
    
    if song_to_find:
        if st.button("search"):
            st.write("searching for song")
            gif_url = "https://cdn.pfps.gg/pfps/2996-toothless-dancing-gif.gif"
            st.image(gif_url)

            return(find_song.song_fingerprint(song_to_find))

