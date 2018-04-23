# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character(_("Elizabeth"), color="#ff9d00")
define d = Character(_("Demon"), color="#000000")
define j = Character(_("Jimbo"), color="#005c87")
define s = Character(_("Mr. Pid"), color="#871400")
define p = Character(_("Principal"), color="#3e8200")

# The game starts here.

label start:

    # catz loves pregnant luigi. lmao

    scene bedroom
    with Dissolve(1.0)

    pause 1.5

    show jimbo sleepy
    with Dissolve(.5)

    pause 1.0

    scene clock
    show jimbo shocked
    # These display lines of dialogue.

    j "FUCK I SLEPT THROUGH MY ALARM"

    "Jimbo frantically pulls on the first clothes they see from the clothes pile on their bedroom floor-
    a T-shirt that reads DOG, jorts, and a mismatched pair of socks."

    show jimbo

    "Jimbo reaches under their bed, pulling out a cheap looking paperback titled DEMON SUMMONING FOR DUMMIES."
    "Flipping to a random page, Jimbo scrawls out a sloppy pentagram on their floor with a hot pink highlighter,
    chants out what's on the page, and bites their thumb so a drop of blood falls on the pentagram."

    scene pentagram

    "A demon appears before them."

    show demon
    with dissolve

    d "what"

    show jimbo

    j "Can you get me to school right now?"
    d "everything has a price, even a mundane wish like that."
    j "So what do I have to give you? Mr. Pid will kill me if I'm late again!"
    "Jimbo glances at the clock, which now reads 7:29."
    j "ShiT, I'll do whatever you want—just send me now please!"
    "The demon flicks her tail in annoyance."
    d "ugh fine. we'll work out the kinks later, i guess."
    "In a flash, Jimbo is suddenly transported to the doorway of their first period class
    just as the bell rings."
    scene classroom door
    show jimbo happy
    j "Yes! Now I can see Elizabeth."
    "Rushing into class, Jimbo sees her—the love of their life, Elizabeth, with her orange
    jumpsuit and strange headband."
    scene classroom
    show elizabeth
    e "Hey what's up Jimbo!"
    show jimbo happy
    j "Sup! Let's give Mr. Pid a bad time as usual. ;)"
    "Exasperated, Mr. Pid runs his hand down his face, and in a deadpan voice,
     calls the classroom to order. Jimbo heads to their seat and sits down, followed
     by the cat."
    hide elizabeth
    show pid

    s "Today we will be covering the Smoot-Hawley act..."
    scene classroom blur
    show pid blur
    show jimbo
    show demon
    "Jimbo immediately tunes Mr. Pid out and looks down quizzically at the cat."
    j "So like, can they see you?"
    d "only if i let them."
    "To prove her point, she leaps on top of Mr. Pid's bald head."
    hide demon
    show pid demon
    "Jimbo motions for the demon to get down, but it just looks like Jimbo is making obscene hand gestures at Mr. Pid."
    "However, Mr. Pid can't muster the energy to tell them to stop, so he
    chooses to ignore Jimbo, whose hand gestures only get more obscene."
    "Jimbo stares at the cat, but the cat just smirks and proceeds to take a
    shit on Mr. Pid's head—a ghostly shit."
    show pid shit
    j "JFC"
    j "Let me help you!"
    show jimbo
    "Jimbo gets up and proceeds to wipe at Mr. Pid's head. To everyone except Jimbo,
    it looks like Jimbo is just massaging Mr. Pid's baldness."
    "Mr. Pid, done with life, just stares at his student. After a long pause, he speaks."
    s "Thanks."
    "Elizabeth walks up and whacks Jimbo on the back of their head."
    show elizabeth right behind jimbo
    e "You numbskull, what the hell are you doing?"
    e "..."
    "Elizabeth joins Jimbo in wiping the beautifully bald head."
    hide pid shit
    "Mr. Pid curls up on the floor to die."
    e "...You killed him..."
    j "..."
    j "But you were doing it, too?"
    "At that moment, the principal walks in."
    show principal shocked
    p "STU!!!"
    "The principal, panicked, rushes to Mr. Pid's side."
    show principal cradling
    "The principal cradles Stu in his arms, weeping over his unmoving body."
    "With his last breaths, Mr. Pid wheezes out his dying words."
    s "We did it...we are a good team..."
    scene black
    with Dissolve(1.0)
    "Without a teacher, Jimbo was sure to fail his next test. Was this the price he
    had to pay to get to school on time?"
    # This ends the game.

    return
