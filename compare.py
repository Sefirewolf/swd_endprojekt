import numpy as np
import convert_mp3 as cmp3

def score_match(offsets):

    differences = [offset[0] - offset[1] for offset in offsets]
    hist, _ = np.histogram(differences, bins='auto')

    return np.max(hist)

def best_match(matches):
    matched_song = None
    top_score = 0

    for song_id, offsets in matches.items(): 
        score = score_match(offsets)
        if score > top_score:
            top_score = score
            matched_song = song_id
    
    return matched_song



def compare_files(audio_file):
    #Compares audiofile to database

    hash = cmp3.generate_hash(audio_file)
    match = get_maches(hash)#funktion in datenbank um alle hashes zu erlangen
    result = best_match(match)

