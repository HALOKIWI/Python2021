class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
"With pockets full of shells"])

abclyrics=["a b c d e f g","h i j k l m n o p"]

abc=Song(abclyrics)

abc.sing_me_a_song()

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

#OOP is programming paradigm that relies on the concept of classes and objects
