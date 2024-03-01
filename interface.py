import streamlit as st
import find_song
import time
import convert_mp3
import datastorage
from database import SongDatabase  # Annahme des Dateinamens für die Datenbankklasse

def add_files_interface():
    uploaded_song = st.file_uploader("Select song from files", type='MP3', 
                                     accept_multiple_files=False, key=None, 
                                     help=None, on_change=None, args=None, 
                                     kwargs=None, disabled=False, label_visibility="visible")
    
    if uploaded_song and st.button("Add MP3"):
        
        
        frequency_list, magnitude_list = convert_mp3.perform_fourier_transform(uploaded_song)
        spectrogram = convert_mp3.create_spectrogram(frequency_list, magnitude_list, 44.1)
        fingerprint = convert_mp3.generate_fingerprints(spectrogram)    
        datastorage.save_fingerprints_to_json(fingerprint, 'fingerprints.json')
        return uploaded_song
    
        
    url_input = st.text_input("Enter the URL of the song you want to add")
    
    
    if st.button("Add URL") and url_input:
        
        
        frequency_list, magnitude_list = convert_mp3.perform_fourier_transform(url_input)
        spectrogram = convert_mp3.create_spectrogram(frequency_list, magnitude_list, 44.1)
        fingerprint = convert_mp3.generate_fingerprints(spectrogram)    
        datastorage.save_fingerprints_to_json(fingerprint, 'fingerprints.json')
        return url_input

def search_song_interface():
    
    
    song_to_find = st.file_uploader("Select song from files", type='MP3', 
                                    accept_multiple_files=False, key=None, 
                                    help=None, on_change=None, args=None, 
                                    kwargs=None, disabled=False, label_visibility="visible")
    
    if song_to_find and st.button("search"):

        st.write("searching for song")

        frequency_list, magnitude_list = convert_mp3.perform_fourier_transform(song_to_find)
        spectrogram = convert_mp3.create_spectrogram(frequency_list, magnitude_list, 44.1)
        fingerprint = convert_mp3.generate_fingerprints(spectrogram)

        # Hier wird der Code hinzugefügt, um die Fingerabdrücke in der Datenbank zu suchen
        # und das Ergebnis zurückzugeben
        result = find_song.song_fingerprint(song_to_find)
        return result
    
    # else : st.error("Upload failed!")

