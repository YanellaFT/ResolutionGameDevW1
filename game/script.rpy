# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Maya")
define n = Character("Narrator")
define ae = Character("Airport Employee")
define d = Character("Droy")

default where_to = "0"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene airport

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Maya stressed

    # These display lines of dialogue.

    n "Maya is stuck in the airport. Her coffee is bad, her phone is at 2 percent, and her flight is delayed, again. "

    n "She is flying to NYC for an important job interview. She had just graduated and really needed this job."

    m "I can't believe this is happening. I need to get to New York! I have an interview tomorrow morning and I can't miss it!"

    show Airport Employee normal

    ae "Ma'am, I'm sorry about your flight delay. I can show you a different flight that is also going to New York, follow me please."

    show Maya confused

    m "Wait, can't you check other flight options on your computer? Why do we have to go somewhere?"

    show Airport Employee normal

    ae "No. You need to follow me..."

    menu:
        "Do you follow the myssterious airport employee?"

        "Yes follow him!":
            $ where_to = "follow_ae"
        "No, don't trust him!":
            $ where_to = "dont_follow_ae"
            jump end

    scene airport two
    
    n "Maya follows the airport employee to a different part of the terminal."

    ae "Here is the flight to New York. You must board now."

    show Maya confused

    m "But.. but my luggage? It's still on the other flight."

    show Airport Employee normal

    ae "Don't worry about it. I'll take care of it for you."

    menu:
        "This is your last chance to not do what this weird guy says. Do you board the flight?"

        "Yes, board the flight!":
            $ where_to = "board_flight"
        "No, don't board the flight!":
            $ where_to = "dont_board_flight"
            jump end


    scene black bg

    n "Maya boards the flight and ..."

    scene dragonia

    show Maya surprised

    n "somehow doesn't enter an airplane?"

    n "While she stepped into a plane on one door side, the other door side is a portal to another world."

    m "Oh... my... what is this place? Where am I?"

    n "The mysterious airport employee is now standing infront of her with a menacing smile. He also doesn't look human anymore."

    show droy normal

    n "He's still in a human body, but he has... dragon wings?!"

    m "You... um, have wings?! And where am I?!"

    d "Welcome to Dragonia, the world of dragons! I am Droy, the human-dragon representative."

    d "My job is to find humans who need a job."

    m "I do need a job... but you just took me away from the one job interview I had a chance in!"

    d "You weren't going to get that job anyways."

    m "Wow. How nice."

    m "Wait, how do you know that?"

    d "I can see the future. Not all of it, but bits and pieces. Anyways, that's not important right now. Don't you wanna know why you are here?"

    menu: 
        "No. I want to go back to my world.":
            $ where_to = "back"
        "Yes. I am kinda intrigued...":
            $ where_to = "stay"

    if where_to == "back":
        d "Too bad too sad. You are here now. You can either become a prisoner or a helper who lives peacefully with us."

    elif where_to == "stay":
        d "Great! Follow me, I'll show you around while we talk."

    n "Droy walks off and you have no choice but to follow."

    show Maya normal

    n "For the first time since the initial shock, Maya gets to look around at her surroundings and take it all in."

    n "There are big green trees everywhere. They have exotic fruits the size of her head growing in all colors. Also on the trees were..."

    scene trees close up

    show Maya surprised

    m "DRAGONS?! Real dragons! Not half human ones!"

    show Droy annoyed

    d "Yes, real dragons. Did you think Dragonia, the world of dragons only had half-dragons?"

    m "Well, um. No? How come you are a half-dragon?"

    d "I've been a human representative for Dragonia for many many hundreds of years. The High King gifted them to me for my service."

    m "Hm. Okay. So... what's my job?"

    show Droy normal

    n "Droy stops abrubtly and turns to Maya, saying:"

    d "Do you see these trees? These plants? These fruits? Humans destroyed these. We need you to save them."

    n "And how exactly do you expect me to save them?"

    d "Well for one, you are going back into the human world to show humans they need to stop littering and control climate change."

    m "Easier said than done..."

    d "Yes. Also, you need to prove yourself to us. That's your first job."

    m "Ookkaayyy... And how?"

    d "Through a series of challenges."

    d "Over the next couple of days you will be presented with a series of challenges to prove you can be a worthy dragon representative."

    show Maya excited

    m "Will I get my own wings?!"

    show Maya sad

    d "Hmpf. No, of course not."

    

    # This ends the game. 

    return


label end:

    show Maya normal

    if where_to == "dont_follow_ae":

        n "Maya decides not to follow the airport employee."
    
    elif where_to == "dont_board_flight":

        n "Maya rethinks her decision to follow the airport employee and decides not to board this new flight."

    n "She goes back to her seat and waits for her flight."
   
    n "She gets on her very delayed flight and almost makes it to her interview on time."

    "The End."

    return