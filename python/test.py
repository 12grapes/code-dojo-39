from song import make_song, song
import pytest

class Test:

    list_of_animals = [
        ("unicorn", "spider"),
        ("rabbit", "spider"),
        ("rabbit", "jackalope"),
    ]

    @pytest.mark.parametrize("animals", list_of_animals)
    def test_make_song(self, animals):
        # Arrange
        (first_animal, second_animal) = animals
        expected_song = song
        expected_song.replace("fly", first_animal)
        expected_song.replace("spider", second_animal)

        # Act
        actual_song = make_song(first_animal, second_animal)
        
        # Assert
        assert actual_song == expected_song
        