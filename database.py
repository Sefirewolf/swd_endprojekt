from tinydb import TinyDB, Query

class SongDatabase:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.songs_table = self.db.table('songs')

    def add_song(self, song_id, song_name, song_interpreter, fingerprinted=False):
        self.songs_table.insert({'song_id': song_id, 'song_name': song_name, 'song_interpreter': song_interpreter, 'fingerprinted': fingerprinted})

    def get_song_by_id(self, song_id):
        Song = Query()
        result = self.songs_table.get(Song.song_id == song_id)
        return result

    def get_all_songs(self):
        return self.songs_table.all()

    def update_fingerprint_status(self, song_id, fingerprinted=True):
        Song = Query()
        self.songs_table.update({'fingerprinted': fingerprinted}, Song.song_id == song_id)

    def get_song_by_fingerprint(self, fingerprint):
        Song = Query()
        result = self.songs_table.get(Song.fingerprint == fingerprint)
        return result

    def close_connection(self):
        self.db.close()

# Pfad erstellen
db_path = '.\database.json' 

# Erstellen einer Instanz der Datenbank
song_db = SongDatabase(db_path)

# Füge ein Lied zur Datenbank hinzu
song_db.add_song(song_id=1, song_name='Example Song 1', song_interpreter='Example Interpreter 1')

# Hol dir alle Lieder in der Datenbank
all_songs = song_db.get_all_songs()
print("Alle Lieder in der Datenbank:", all_songs)

# Aktualisiere den Fingerprint-Status für ein Lied
song_db.update_fingerprint_status(song_id=1, fingerprinted=True)

# Schließe die Datenbank-Verbindung
song_db.close_connection()
