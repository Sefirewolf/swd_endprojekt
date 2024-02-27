import json

def save_fingerprints_to_json(fingerprints, filename):
    with open(filename, 'w') as f:
        json.dump(fingerprints, f)