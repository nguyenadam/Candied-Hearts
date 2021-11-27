# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Hansel", color="#C9A869")
define g = Character("Gretel", color="#B469C9")
define witch = Character("Wicked Witch", color="#262e99")

# game wide variables
default hansel_relationship = 0
default gretel_relationship = 0

# style
transform midright:
    xalign 0.7
transform midleft:
    xalign 0.3

label start:
    # change to introduction on build
    jump dev

label dev:
    menu:
        "Intro":
            jump introduction
        "Day 1":
            jump d1