from pytube import YouTube
from pydub import AudioSegment
import pygame
import os



class video_download_and_convert():
    
    def __init__(self, filepath, filename):
        
        self.filepath = filepath
        self.filename = filename

    def download_video(self, url, destination):
        try:
            # YouTube-Objekt erstellen
            youtube = YouTube(url)

            # Video stream auswählen
            video_stream = youtube.streams.get_highest_resolution()

            # Video herunterladen
            
            
            video_filepath = video_stream.download(destination)
            
            actual_filename = youtube.title + "." + video_filepath.split(".")[-1]


            print(f"Das Video wurde erfolgreich heruntergeladen und unter {destination} gespeichert.")
        except Exception as e:
            print(f"Fehler beim Herunterladen des Videos: {e}")



    def convert_mp4_to_mp3_and_play(self, input_directory, output_directory):
        try:
            # Iterate through all files in the input directory
            for filename in os.listdir(input_directory):
                # Check if the file has a .mp4 extension
                if filename.endswith(".mp4"):
                    # Construct the full path for the input file
                    input_path = os.path.join(input_directory, filename)

                    # Construct the full path for the output file (change extension to .mp3)
                    output_path = os.path.join(output_directory, filename[:-4] + ".mp3")

                    # Convert and play the MP3 file
                    self._convert_and_play(input_path, output_path)

            print("Conversion and playback of all eligible files completed.")
        except Exception as e:
            print(f"Error during conversion and playback: {e}")

    def _convert_and_play(self, input_path, output_path):
        # Lade die MP4-Datei
        audio = AudioSegment.from_file(input_path, format='mp4')

        # Speichere die MP3-Datei
        audio.export(output_path, format='mp3')

        print(f"The MP4 file has been successfully converted to MP3 and saved at {output_path}.")

        # Spiele die MP3-Datei ab
        pygame.mixer.init()
        pygame.mixer.music.load(output_path)
        pygame.mixer.music.play()

        # Warte bis das Audio abgespielt wurde
        pygame.time.Clock().tick(10)  # Einfacher Timer, um das Programm laufen zu lassen
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)



new_video = video_download_and_convert(".\youtube_files", "https://www.youtube.com/watch?v=GlLJ0yd_QvI&ab_channel=HBz")

new_video.download_video(".\youtube_files", "https://www.youtube.com/watch?v=GlLJ0yd_QvI&ab_channel=HBz")


new_video.convert_mp4_to_mp3_and_play(".\youtube_files", ".\youtube_files"  )