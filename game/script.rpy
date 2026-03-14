# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Maya")
define n = Character("Narrator")
define ae = Character("Airport Employee")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Maya stressed

    # These display lines of dialogue.

    n "Maya is stuck in the airport. Her coffee is bad, her phone is at 2 percent, and her flight is delayed, again. "

    n "She is flying to NYC for an important job interview. She had just graduated and really needed this job."

    # n "Maya goes to talk to an airport employee to see if there is anything they can do about her flight delay."

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
            jump follow_ae
        "No, don't trust him!":
            jump dont_follow_ae

    # This ends the game.

    return

label follow_ae:

    show Maya normal
    
    n "Maya follows the airport employee to a different part of the airport. It's ... to be continued ..."
    
    return

label dont_follow_ae:

    show Maya normal

    n "Maya decides not to follow the airport employee. She goes back to her seat and waits for her flight."
   
    n "She gets on her very delayed flight and almost makes it to her interview on time."
    
    return