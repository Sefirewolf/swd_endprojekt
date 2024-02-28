import streamlit as st
from streamlit_option_menu import option_menu
import interface
import convert_mp3
import librosa
import matplotlib.pyplot as plt
import numpy as np

def perform_fourier_transform(audio_file):
    # Load the MP3 file
    y, sr = librosa.load(audio_file)

    # Apply Fourier Transform
    fft_output = np.fft.fft(y)

    # Frequency domain representation
    magnitude = np.abs(fft_output)
    frequency = np.fft.fftfreq(len(magnitude), d=1/sr)

    return frequency[:len(frequency)//2], magnitude[:len(frequency)//2]




def main():
    st.title("Shantzahn")

    selected = option_menu(
        None,
        ["Find Song", "Add MP3-Files"],
        icons=['search', 'filetype-mp3'],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal"
    )

    if selected == "Add MP3-Files":
        new_song = interface.add_files_interface()
        st.write(f"Added {new_song}")


    elif selected == "Find Song":
        song_title = interface.search_song_interface()
        if(song_title):
            st.text(f"The Title of the song is {song_title}\nThe artist is unknown")



if __name__ == "__main__":
    main()