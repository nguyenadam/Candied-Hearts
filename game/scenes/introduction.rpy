label introduction:    
    show black
    "Deep in the Black Forest, in a house made of candy, a wicked witch worries."
    witch "Where is it?"
    show room interior
    with fade
    with hpunch
    witch "I know I put them {i}somewhere{/i}, where are they?!"
    "..."
    with hpunch
    "..."
    with hpunch
    witch "Curses…"
    witch "Where are those vials?"

    menu:
        "Look in the ingredients cabinet.":
            jump cabinet
        "Look in the potions rack.":
            jump rack
        "Look in the pantry.":
            jump pantry

label cabinet:
    "You look through your ingredients cabinet, but all you find are flowers and frog legs!"
    jump intro2

label rack:
    "You look through your potions rack, but all you find are half-baked concoctions and empty glass vials."
    jump intro2

label pantry:
    "You look through your pantry, but all you find is a slew of baking ingredients!"
    jump intro2

label intro2:
    "You continue your search, turning your candied house upside-down in search of those vials, but to no avail."
    witch "I can't be out of childsblood! The solstice draws ever nearer, I don't have time to get more!"
    "As the septennium comes to an end, you can already feel the immortality fading from your brittle bones. If you don't find the childsblood you seek, you'll crumble to dust as you should 
    have all those years ago."

    menu:
        "I'll sneak into town and steal it.":
            jump town
        "I'll ask a child for their blood nicely.":
            jump ask
        "I'll host a blood drive!":
            jump drive

label town:
    witch "I'll sneak into town and {i}steal{/i} the childsblood!"
    witch "It's a perfectly evil and foolproof plan!"
    "But it wasn't a perfectly evil and foolproof plan."
    "It was certainly evil, but the nearest town was days away."
    jump intro3

label ask:
    witch "Maybe I can ask a child for their blood. I can be nice!"
    witch "..."
    witch "Who am I kidding, no child would willingly give up their blood."
    witch "And besides, I don't see many children around here."
    witch "..."
    jump intro3

label drive:
    witch "Maybe I'll run a blood drive! It's always worked well for the vampires."
    "You're briefly excited, but you soon remember that you live in the middle of nowhere and scrap the idea. Besides, who takes their children to a blood drive?"
    jump intro3

label intro3:
    witch "What to do, what to do?"
    play sound knocking
    "Just then, you hear a small knock at the door."
    h "Hello?"
    "A small boy calls inside as he knocks."
    "Perfect..."
    witch "Ah, yes, coming dearie!"
    "You immediately put on your nicest, least-witchy face, and open the door to the solution to all of your problems."
    show kids
    witch "There's two of you?"
    h "Ma'am, may we please spend the night! It's getting dark outside and we need a place to stay!"
    witch "Oh, why, yes! Come on in, come on in, both of you! The more the merrier!"
    "Brats."
    "But brats with childsblood."
    "And between the two, they'll certainly have enough for the ceremony."
    "You'll just need to fatten 'em up before the big day."
    "And you know just the way to do it."
    witch "Say, are you two hungry? I've got some cake inside!"
    h "Cake?!"
    "You smile."
    "This'll be as easy as cake."
    "..."
    "Wait…"
    show black
    with fade