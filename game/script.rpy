# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Andonn")


# The game starts here.

label start:
    play music "audio/Desert sound - Sound effect.mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg desert
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    e "It is a hot day in a desert, and I walk around just to fulfill my curiosity."

    e "Suddenly, I saw something from the distance."

    "<walk further>"

    scene bg desert box
    with fade 
    play music "audio/ES_Sand Storm - SFX Producer.mp3"

    e "I found a container room, in the middle of a desert."

    e "The container room has a door and some stairs behind it."

    menu:

        e "I’m curious so I decided..."

        "To go down stairs.":

            jump downstairs 

label downstairs:
    play music "audio/Kevin Macleod SPC x2x Unseen Presence.mp3"
    scene bg basement
    with fade 

    e "Wow! There’s a secret room below the container room."

    e "There’s a door and a stair right in front of me."

    e "Wait! I hear a voice from the distance, what is it?"

    menu:

        e "I’m curious so I decided..."

        "To go through door.":

            jump lava

        "Avoid the door and take the stairs.": 
            jump mainRoom

label lava:
    play music "audio/Kevin Macleod SCP x3x - I am Not OK.mp3"
    scene bg lava
    with fade 

    e "Ah! It’s very hot in here!"

    e "It turns out that this place is full of lava."
    
    menu:

        e "I need to..."

        "Go back!":

            jump downstairs2

label downstairs2:
    play music "audio/Kevin Macleod SPC x2x Unseen Presence.mp3"
    scene bg basement
    with fade 

    e "Thank God I’m still alive!"

    e "The lava was dangerous back there!"

    menu: 

        e "I’m not going back there, I think I’ll..."

        "Take the stair instead.":
            jump mainRoom 

label mainRoom: 
    scene bg bunker
    with fade 
    play music "audio/ES_Abandoned Warehouse - SFX Producer.mp3"

    e "Where am I?"

    e "Why is there a hallway, another door, and stairs?"

    menu:
        e "I need to know what’s next, so I decided..."

        "To open door.":
            jump spiderRoom
        
        "To go down hallway.":
            jump ending

label spiderRoom:
    scene bg twodoors
    with fade
    
    play music "Big Drumming.mp3"
    
    e "What room is it?"    

    "Something appeared.."

    show sprite spider 

    e "Oh my God! There’s a big spider!"

    e "I’m afraid of spiders, so I don’t want to fight it."

    menu:
        e "I want to run away from it, so I choose..."

        "The left door.":
            jump mainRoom
        
        "The right door.":
            jump ending

label mainRoom1:
    scene bg bunker
    with fade 
    play music "audio/ES_Abandoned Warehouse - SFX Producer.mp3"

    e "Lucky me, I don’t have to fight that spider!"

    menu:
        e "I need to know what’s next, so I decided..."

        "To go down hallway.":
            jump ending

        "To open door.":
            jump spiderRoom

label spiderRoom1:
    scene bg twodoors
    with fade 
    play music "audio/Big Drumming.mp3"

    e "What room is it? looks familiar"    

    "Something appeared.."

    show sprite spider 

    e "Oh my God! There’s a big spider again!"

    menu:
        e "I want to run away from it, so I choose..."

        "The left door.":
            jump mainRoom
        
        "The right door.":
            jump ending

label ending:
    play music "audio/MusMus-BGM-096.mp3"
    scene bg hallway
    with fade 

    e "What the luxurious room!"

    e "This luxurious room got hallway, door, and chairs."

    menu:
        e "Where should I go next? Maybe I should..."

        "Go to the hallway":
            jump mainRoom

        "Go to the door": 
            jump spiderRoom1

        "Sit on the chair.":
            play music "audio/Angel - Sound Effect (HD).mp3"  
            scene bg gold chest
            with fade 
            e "Ouch! Something just falls down from the ceiling."
            e "It looks like a chest, let me open it…"
            play music "audio/ES_Coins Drop Pirate Gold - SFX Producer.mp3"  
            scene bg gold
            with fade 
            e "Oh yes! I just found some gold!"
            e "What a lucky person I am!"

    # This ends the game.
    return


