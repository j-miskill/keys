import get_song
import pytest


class Test_All:

    # test reading in the json data
    def test_read_in_data(self):
        test_data = get_song.read_in_keys_and_chords()
        assert test_data is not None
        assert "keys" in test_data.keys()
        assert "major" in test_data['keys'].keys() and "minor" in test_data['keys'].keys()
        assert type(test_data['keys']['major']) == list
        assert type(test_data['keys']['minor']) == list

    def test_get_keys_from_data(self):
        test_data = get_song.read_in_keys_and_chords()
        test_keys = get_song.get_keys_from_data(test_data)

        assert type(test_keys) == list
        assert len(test_keys) == 24
        assert type(test_keys[0]) == str