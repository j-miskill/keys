import os.path
import random
import json
from pprint import pprint


def read_in_keys_and_chords():
    keys_and_chords = {}
    if os.path.isfile("keys.json"):
        f = open("keys.json")
        keys_and_chords = json.load(f)
        f.close()
    else:
        raise FileNotFoundError("Please create key file")
    return keys_and_chords


def get_keys_from_data(keys_and_chords_data):
    keys = []

    def add_in_major_keys():
        for k in keys_and_chords_data['keys']['major']:
            key, value = list(k.items())[0]
            keys.append(key)

    def add_in_minor_keys():
        for k in keys_and_chords_data['keys']['minor']:
            key, value = list(k.items())[0]
            keys.append(key)

    add_in_major_keys()
    add_in_minor_keys()
    return keys


def pick_key(keys):
    r = random.randint(0, 23)
    k = keys[r]
    return k


def find_chords(key, keys_and_chords_data):
    chords = []

    def search_major():
        for k in keys_and_chords_data['keys']['major']:
            temp_key, value = list(k.items())[0]
            if temp_key == key:
                return value

    def search_minor():
        for k in keys_and_chords_data['keys']['minor']:
            temp_key, value = list(k.items())[0]
            if temp_key == key:
                return value

    chords = search_major()
    if chords is None:
        chords = search_minor()

    if chords is None:
        raise Exception("No chords found for some reason")
    return chords


def generate_song(chords):
    print("Generating song with these chords:", chords)
    def generate_lines():
        # could ask for how many lines
        return random.randint(0, 42)

    def generate_number_chords_per_line():
        # could ask for how many chords per line
        # or to find a random number of chords per line
        return random.randint(0, 11)

    def get_random_chord(chords):
        r = random.randint(0, len(chords)-1)
        return chords[r]

    lines = generate_lines()
    chords_per_line = generate_number_chords_per_line()

    # could implement something like "name" for the output file name
    f = open("songs/song.txt", "a")

    for l in range(0, lines):
        progression = ""
        for c in range(0, chords_per_line):
            chord = get_random_chord(chords)
            progression = progression + chord + " "

        f.write(progression)
    f.close()
    print('done')


def run():
    # read in all the keys and chords
    keys_and_chords_data = read_in_keys_and_chords()

    # get a single list of all of the keys
    keys = get_keys_from_data(keys_and_chords_data)

    # randomly pick a key from that single list of all keys
    key = pick_key(keys)

    # get the list of all chords in that key
    chords = find_chords(key, keys_and_chords_data)

    # generate a random song with those chords
    # lines, number of chords per line
    generate_song(chords)


if __name__ == "__main__":
    # just going to do a baseline randomized thing right now, will add CLAs later
    run()
