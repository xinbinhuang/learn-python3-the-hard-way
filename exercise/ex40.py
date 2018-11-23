# OOP

## 1. Dictionary
## =================================
mystuff = {'apple': 'I AM APPLES!'}
print(mystuff['apple'])


## 2. Module
## =================================
import mystuff

mystuff.apple()
print(mystuff.tangerine)

## 3. Class
## =================================

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES")


thing = MyStuff()  # 'instantiate' an object

thing.apple()
print(thing.tangerine)


print("-" * 30)
print('Our First class object')
print("-" * 30)


class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


lyrics_happy = [
    "Happy birthday to you",
    "I don't want to get sured",
    "So I'll stop right there"
]
happy_bday = Song(lyrics_happy)

lyrics_bulls = [
    "They rally around that family",
    "With pockets full of shells"
]
bulls_on_parade = Song(lyrics_bulls)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
