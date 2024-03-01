from tinydb import TinyDB, Query
import convert_mp3
import os

class SongDatabase:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.songs_table = self.db.table('songs')

    def add_song(self, song_id, song_name, fingerprinted=False):
        self.songs_table.insert({'song_id': song_id, 'song_name': song_name, 'fingerprinted': fingerprinted})

    def add_songs(self, song_id, titel, interpret, audio_file):

        fingerprint = convert_mp3.generate_hash(audio_file)
        self.songs_table.insert({'id:': song_id, 'name': titel, 'interpret': interpret, 'hash': fingerprint} )

    def get_song_by_id(self, song_id):
        Song = Query()
        result = self.songs_table.get(Song.song_id == song_id)
        return result

    def get_all_songs(self):
        return self.songs_table.all()

    def update_fingerprint_status(self, song_id, fingerprinted=True):
        Song = Query()
        self.songs_table.update({'fingerprinted': fingerprinted}, Song.song_id == song_id)

    def delete_entries(self):
        self.db.drop_tables()

    def close_connection(self):
        self.db.close()

# Pfad erstellen
db_path = '.\database.json' 

# Erstellen einer Instanz der Datenbank
song_db = SongDatabase(db_path)

# Füge ein Lied zur Datenbank hinzu
#song_db.add_song(song_id=1, song_name='Example Song 1')
song_db.add_songs(1, "Numb", "Linkin Park", "C:/Users/philz/swd_endprojekt/youtube_files/Numb.mp3")

#song_db.delete_entries()

"""audio_file = "C:/Users/philz/swd_endprojekt/youtube_files/Numb.mp3"
if os.path.exists(audio_file):
    print("Die Datei existiert.")
else:
    print("Die Datei existiert nicht oder der Pfad ist falsch.")"""

# Hol dir alle Lieder in der Datenbank
all_songs = song_db.get_all_songs()
print("Alle Lieder in der Datenbank:", all_songs)

# Aktualisiere den Fingerprint-Status für ein Lied
song_db.update_fingerprint_status(song_id=1, fingerprinted=True)


# Schließe die Datenbank-Verbindung
song_db.close_connection()
