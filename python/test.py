from song import make_song, song
import pytest

# Fixtures
unicorn = {"name": "unicorn", "rhyme": "They love acorn!"}
spider = {"name": "spider", "rhyme": "she wiggled and wiggled inside her!"}
rabbit = {"name": "rabbit", "rhyme": "that's a funny habit!"}
jackalope = {"name": "jackalope", "rhyme": "there is no hope..."}

class Test:

    list_of_animals = [
        (unicorn, spider),
        (rabbit, spider),
        (rabbit, jackalope),
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
        