def make_song(first_animal, second_animal):
    first_animal_name = first_animal.get("name")
    second_animal_name = second_animal.get("name")
    second_animal_rhyme = second_animal.get("rhyme")

    song = f"""There was an old lady who swallowed a {first_animal_name}.
I don't know why she swallowed a {first_animal_name} - perhaps she'll die!

There was an old lady who swallowed a {second_animal_name};
{second_animal_rhyme}
She swallowed the {second_animal_name} to catch the {first_animal_name};
I don't know why she swallowed a {first_animal_name} - perhaps she'll die!

There was an old lady who swallowed a bird;
How absurd to swallow a bird.
She swallowed the bird to catch the {second_animal_name},
She swallowed the {second_animal_name} to catch the {first_animal_name};
I don't know why she swallowed a {first_animal_name} - perhaps she'll die!

There was an old lady who swallowed a cat;
Fancy that to swallow a cat!
She swallowed the cat to catch the bird,
She swallowed the bird to catch the {second_animal_name},
She swallowed the {second_animal_name} to catch the {first_animal_name};
I don't know why she swallowed a {first_animal_name} - perhaps she'll die!

There was an old lady who swallowed a dog;
What a hog, to swallow a dog!
She swallowed the dog to catch the cat,
She swallowed the cat to catch the bird,
She swallowed the bird to catch the {second_animal_name},
She swallowed the {second_animal_name} to catch the {first_animal_name};
I don't know why she swallowed a {first_animal_name} - perhaps she'll die!

There was an old lady who swallowed a cow;
I don't know how she swallowed a cow!
She swallowed the cow to catch the dog,
She swallowed the dog to catch the cat,
She swallowed the cat to catch the bird,
She swallowed the bird to catch the {second_animal_name},
She swallowed the {second_animal_name} to catch the {first_animal_name};
I don't know why she swallowed a {first_animal_name} - perhaps she'll die!

There was an old lady who swallowed a horse...
...She's dead, of course!"""
    return song
