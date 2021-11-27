# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Hansel", color="#C9A869")
define g = Character("Gretel", color="#B469C9")
define witch = Character("Wicked Witch", color="#262e99")

default hansel_relationship = 0
default gretel_relationship = 0

# The game starts here.
# DAY 0
# ---------

label start:
    jump introduction