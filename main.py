import streamlit as st
from streamlit_option_menu import option_menu
import interface


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
        song_title, song_artist = interface.search_song_interface()
        if(song_title):
            st.text(f"The Title of the song is {song_title}\nThe artist is {song_artist}")



if __name__ == "__main__":
    main()