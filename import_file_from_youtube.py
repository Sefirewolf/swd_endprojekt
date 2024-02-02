from pytube import YouTube

def download_video(url, destination):
    try:
        # YouTube-Objekt erstellen
        youtube = YouTube(url)

        # Video stream auswählen
        video_stream = youtube.streams.get_highest_resolution()

        # Video herunterladen
        video_stream.download(destination)

        print(f"Das Video wurde erfolgreich heruntergeladen und unter {destination} gespeichert.")
    except Exception as e:
        print(f"Fehler beim Herunterladen des Videos: {e}")

# Beispiel-URL und Zielort für das heruntergeladene Video
url = 'https://www.youtube.com/watch?v=x2rQzv8OWEY&ab_channel=RammsteinOfficial'
zielort = ".\youtube_files" 

# Funktion aufrufen, um das Video herunterzuladen
download_video(url, zielort)
