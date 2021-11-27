label d1:
    scene room interior with fade
    "It's a beautiful morning in the Black Forest."
    
    "The sun is shining, the birds are singing, and the forest animals are eating your candy house. What a nice, peaceful-"
    
    with hpunch

    witch "{i}SHOO YOU FILTHY ANIMALS!{/i}"

    "A doe stares at you as it presses its tongue against your sugar glass window panes, undisturbed and completely unshooed."
    
    witch "Go on! Git! Sugar glass ain't cheap, ya know!"
    
    "You smack the glass a few times, but the deer continues its lazy destruction of property."
    
    show hansel stunned at midleft with easeinleft
    
    h "What's going on?!"
    
    witch "Those darn animals are eating my house again!"
    
    h "Ma'am, please!"
    
    witch "What?"
    
    show gretel scared at midright with easeinright
    
    g "..."

    menu:
        "Are you okay?":
            jump d1_o1
        "What's with her?":
            jump d1_o2

label d1_o1:
    witch "Are you okay? What's wrong?"
    $ hansel_relationship += 1;
    $ gretel_relationship += 1;
    show hansel quiet
    h "She doesn't like shouting."
    g "..."
    "Pretending to be nice is really grating on you. And a child who doesn't like shouting? Why, that's preposterous! It's so much fun!"
    witch "Oh, sorry dear. But these animals! They keep munching on my house! One of these days they're gonna nibble through something load-bearing and..."
    "You stop yourself, seeing Gretel's teary eyes."
    witch "Well, that's not important now, is it?"
    jump D1_1


 
label d1_o2:
    witch "What's with her?"
    $ hansel_relationship -= 2;
    $ gretel_relationship -= 1;
    show hansel shouting
    with hpunch
    h "Ma'am!"
    with hpunch
    witch "What?!"
    show gretel scared
    g "Eek!"
    show hansel quiet
    h "Gretel… doesn't like shouting."
    witch "But..."
    witch "..."
    "You were going to argue that the animals wouldn't listen to you if you didn't startle them a little, but that clearly wasn't working anyway. And looking back at the teary-eyed girl…"
    jump D1_1

label D1_1:
    show gretel quiet
    "You kneel down beside the girl and put a comforting hand on her shoulder."
    witch "Tell you what--how about you go take care of that deer for me, okay? Your brother and I will be inside with some cookies for you when you're done, okay?"
    show hansel suspicious
    h "We--what? What about breakf-"
    witch "Cookies! Fun! Now, go take care of that deer!"
    show gretel bright_eyed
    g "Okay!"
    hide gretel with moveoutright
    "Gretel leaves with a sudden pep in her step."
    hide hansel with moveoutleft
    "A moment later, you can see her through the sugar glass gently leading the doe away from your windows. An excited awe simmers beneath her controlled calm, as to not frighten the animal."
    "By the time Gretel's led the deer away, Hansel's tugging on your sleeve."
    show hansel embarrassed
    h "I'm… sorry for yelling at you."
    witch "Oh, that's--"
    "You're about to tell him you didn't care when a loud munching comes from one of the walls."
    with hpunch
    show hansel quiet
    witch "HEY YOU NASTY CRITTERS! CUT IT OUT!"
    h "Maybe… let's just go make some breakfast."
    witch "Yes, the cookies!"
    h "Yeah… cookies…"
    hide hansel with fade

    scene bg kitchen with fade
    "While Gretel's busy taking care of the animals outside, you and Hansel make the cookie dough and drop dollops onto a metal tray."
    show hansel quiet
    h "I still think we shouldn't have cookies for breakfast."
    witch "Nonsense! If you bake them yourself, they're {i}your{/i} calories--perfectly healthy!"
    "Plus, it couldn't hurt to fatten up these kids a bit before the ceremony."
    h "..."
    h "Do you even have any real food in this house? It's like everything here is made out of sugar."

    menu:
        "Sugar {i}is{/i} a real food!":
            jump d1_o2_1
        "Probably?":
            jump d1_o2_2

label d1_o2_1:
    witch "Sugar {i}is{/i} a real food!!"
    witch "It's one of the four basic food groups: Sugar, Chocolate, Cookies, and Jelly Beans!"
    show hansel suspicious
    h "Thats'… not even remotely true."
    witch "What? Of course it is--what are they teaching you kids these days?"
    show hansel saddened
    h "Fractions… lots of fractions…"
    witch "Well {i}that's{/i} why you don't know anything about proper nutrition!"
    show hansel suspicious
    h "No, I still think I'm right about that…"
    $ hansel_relationship += 2;
    jump D1_2

label d1_o2_2:
    witch "Probably?"
    show hansel suspicious
    h "You don't {i}know{/i}?"
    witch "It's never come up before! No one's ever complained about my baking."
    "Hansel looks at you in surprise."
    h "Other people have been here?"
    witch "Well, no, but that's beside the point! And what's with you, I thought you kids {i}liked{/i} sugar!"
    show hansel saddened
    h "I… just want to make sure Gretel eats enough."
    witch "Well she\'ll certainly want to eat enough of these cookies!"
    "You smile as you lift up your tray; balls of dough cover the tray in neat rows."
    h "..."
    $ hansel_relationship += 1;
    jump D1_2

label D1_2:
    "You and Hansel both slide your cookie trays into the oven. Once you\'ve set the timer, Gretel comes back inside"
