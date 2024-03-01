import streamlit as st
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from database import SongDatabase

def perform_fourier_transform(audio_file, frame_size=2048):
    # Load the MP3 file
    y, sr = librosa.load(audio_file, sr=None)

    # Calculate the number of frames
    num_frames = len(y) // frame_size

    # Initialize arrays to store frequency and magnitude
    frequency_list = []
    magnitude_list = []

    # Apply Fourier Transform to each frame
    for i in range(num_frames):
        start = i * frame_size
        end = start + frame_size
        frame = y[start:end]

        # Apply Fourier Transform
        fft_output = np.fft.fft(frame)

        # Frequency domain representation
        magnitude = np.abs(fft_output)
        frequency = np.fft.fftfreq(frame_size, d=1/sr)

        # Append to lists
        frequency_list.append(frequency[:frame_size//2])
        magnitude_list.append(magnitude[:frame_size//2])

    return frequency_list, magnitude_list

def create_spectrogram(frequency_list, magnitude_list, sr):
    # Initialize an empty spectrogram
    spectrogram = []

    # Iterate over each frame and create its spectrogram
    for frequency, magnitude in zip(frequency_list, magnitude_list):
        # Convert frequency and magnitude to dB scale
        magnitude_db = librosa.amplitude_to_db(magnitude, ref=np.max)

        # Append the spectrogram for the frame to the overall spectrogram
        spectrogram.append(magnitude_db)

    # Convert the list of spectrograms to a numpy array
    spectrogram = np.array(spectrogram)

    return spectrogram

def generate_fingerprints(spectrogram, threshold=0, song_db=None):
    # Define parameters
    window_size = 3  # Adjust as needed
    hop_length = 1   # Adjust as needed

    # Initialize list to store fingerprints
    fingerprints = []

    # Iterate over spectrogram to generate fingerprints
    for i in range(len(spectrogram) - window_size):
        # Get current and adjacent windows
        window = spectrogram[i:i+window_size]

        # Find peaks above threshold in current window
        peaks = find_peaks(window, threshold)

        # Generate fingerprints for each peak
        for peak in peaks:
            fingerprint = generate_fingerprint(peak, window)

            # Anpassung: Speichern Sie den Fingerabdruck in der Datenbank
            save_fingerprint_to_db(fingerprint, i, song_db)

    return fingerprints

def find_peaks(window, threshold):
    # Find peaks above threshold in the window
    peaks = []
    for freq in range(len(window)):
        if np.any(window[freq] > threshold):
            peaks.append(freq)
    return peaks

def generate_fingerprint(peak, window):
    # Generate fingerprint for the peak based on nearby peaks in adjacent windows
    fingerprint = []
    for freq in range(max(0, peak-1), min(len(window[0]), peak+2)):
        for time in range(len(window)):
            if window[time][freq] > 0:
                fingerprint.append((freq, time))
    return fingerprint

def save_fingerprint_to_db(fingerprint, i, song_db):
    # Annahme: song_db ist eine Instanz Ihrer Datenbankklasse (SongDatabase)
    # Annahme: Der Fingerabdruck wird als Tupel (i, fingerprint) übergeben

    # Beispiel: Annahme, dass song_id und song_name bekannt sind
    song_id = 1
    song_name = 'Example Song 1'

    # Füge den Fingerabdruck zur Datenbank hinzu
    song_db.add_song(song_id=song_id, song_name=song_name, fingerprinted=True)
