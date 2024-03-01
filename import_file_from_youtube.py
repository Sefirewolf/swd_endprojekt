from pytube import YouTube
from pydub import AudioSegment
import os
import string

class VideoDownloadAndConvert:
    
    def __init__(self, output_directory):
        self.output_directory = output_directory

    def download_video_and_convert_to_mp3(self, url):
        try:
            
            youtube = YouTube(url)
            
            video_stream = youtube.streams.get_highest_resolution()
            video_filepath = video_stream.download(self.output_directory)
            filename = self._sanitize_filename(youtube.title)
            
            mp3_output_path = os.path.join(self.output_directory, f"{filename}.mp3")
            self._convert_to_mp3(video_filepath, mp3_output_path)
            
            
            print(f"Video downloaded and converted to MP3. MP3 file saved at {mp3_output_path}.")
            os.remove(video_filepath)
            print(f"Original MP4 file has been deleted.")
            
            
        except Exception as e:
                     
            print(f"Error during download and conversion: {e}")
                 

    def _convert_to_mp3(self, input_path, output_path):
        
        
        try:
            
            audio = AudioSegment.from_file(input_path, format='mp4')
            audio.export(output_path, format='mp3')
            print(f"The video has been successfully converted to MP3 and saved at {output_path}.")
                       
        except Exception as e:      
            
            print(f"Error during MP4 to MP3 conversion: {e}")

    def _sanitize_filename(self, title):
          
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        filename = ''.join(char for char in title if char in valid_chars)
        return filename[:255]
    

# Beispiel-Nutzung: output directory durch gewünschten speicherodner ersetzen

output_directory = "C:\\Users\\User\\Documents\\MCI\\Softwaredesign_WS23\\001_Abschlussprojekt\\swd_endprojekt\\youtube_files"
video_processor = VideoDownloadAndConvert(output_directory)

#unten url hinzufügen

video_url = "https://www.youtube.com/watch?v=v2AC41dglnM&ab_channel=acdcVEVO"

video_processor.download_video_and_convert_to_mp3(video_url)
