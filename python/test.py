import song
import pytest

class Test:
    def test_make_song(self):
        assert song.make_song() == song.song 

    def test_split_song(self):
        assert song.split_aong() == ["gagaga"]