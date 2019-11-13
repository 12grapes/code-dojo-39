from song import make_song
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
    def test_make_song_replaces_animals_names(self, animals):
        # Arrange
        (first_animal, second_animal) = animals

        # Act
        actual_song = make_song(first_animal, second_animal)

        # Assert
        assert first_animal.get("name") in actual_song
        assert second_animal.get("name") in actual_song

    @pytest.mark.parametrize("animals", list_of_animals)
    def test_make_song_replaces_rhyme(self, animals):
        # Arrange
        (first_animal, second_animal) = animals

        # Act
        actual_song = make_song(first_animal, second_animal)

        # Assert
        assert not first_animal.get("rhyme") in actual_song
        assert second_animal.get("rhyme") in actual_song
