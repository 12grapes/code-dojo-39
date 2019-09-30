import song
import pytest

class Test:
    def test_make_song(self):
        assert song.make_song() == song.song 

    def test_unicorn(self):
        assert song.animal_song('unicorn') == unicorn_song

    def test_rabbit(self):
        assert song.animal_song('rabbit') == unicorn_song
    
unicorn_song = """There was an old lady who swallowed a unicorn.
I don't know why she swallowed a unicorn - perhaps she'll die!

There was an old lady who swallowed a spider;
That wriggled and wiggled and tickled inside her.
She swallowed the spider to catch the unicorn;
I don't know why she swallowed a unicorn - perhaps she'll die!

There was an old lady who swallowed a bird;
How absurd to swallow a bird.
She swallowed the bird to catch the spider,
She swallowed the spider to catch the unicorn;
I don't know why she swallowed a unicorn - perhaps she'll die!

There was an old lady who swallowed a cat;
Fancy that to swallow a cat!
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider,
She swallowed the spider to catch the unicorn;
I don't know why she swallowed a unicorn - perhaps she'll die!

There was an old lady who swallowed a dog;
What a hog, to swallow a dog!
She swallowed the dog to catch the cat,
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider,
She swallowed the spider to catch the unicorn;
I don't know why she swallowed a unicorn - perhaps she'll die!

There was an old lady who swallowed a cow;
I don't know how she swallowed a cow!
She swallowed the cow to catch the dog,
She swallowed the dog to catch the cat,
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider,
She swallowed the spider to catch the unicorn;
I don't know why she swallowed a unicorn - perhaps she'll die!

There was an old lady who swallowed a horse...
...She's dead, of course!"""
