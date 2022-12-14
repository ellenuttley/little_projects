import random
import time

while True:

    your_day_x = ("good", "bad", "beautiful", "harrowing", "boring", "normal", "amazing", "stressful", "fantastical", "stupendous")
    favourite_place_x = ("the nail salon", "disneyland", "the aquarium", "the museum", "the ice rink", "the soda hop", "the cinema", "the pub")
    favourite_person_x = ("Grandma", "Mr T", "Professor X", "Chris Hemsworth", "Harry Potter", "Santa Claus", "Spiderman", "Bob Ross", "Mark Zuckerbergs Mum")
    something_scary_x = ("cows", "spiders", "vampires", "zombies", "rabid dogs", "rotten fish", "go-go boots", "rotten eggs", "Mark Zuckerbergs")
    time_of_day_x = ("morning", "night time", "dinner time", "tea time", "breakfast time", "twilight", "dusk", "sunrise", "sunset")
    animal_x = ("crocodile", "dinosaur", "goat", "snake", "komodo dragon", "racoon", "red panda", "sloth", "tiger", "hippo", "alley cat", "bear", "yeti")
    something_deep_x = ("quarry", "void", "black hole", "vortex", "well", "river", "hellish pit")

    print('''

    Welcome to MadLibs ... ''')

    time.sleep(1)

    print('''
    Things are about to get MAD
    ''')

    time.sleep(1)

    your_name = input("To start the madness, please enter your name: ").title()

    time.sleep(1)

    pronoun_input = input("What are your pronouns?: ").lower()

    while pronoun_input.find("/") == -1:
                    print('''I am so sorry... I don't understand that. 
            
            Please enter pronouns in format ---/---''')
                    pronoun_input = input("What are your pronouns?: ").lower()
                    if pronoun_input.find("/") != -1:
                        break

    pronouns = pronoun_input.split('/')
    she_pronoun = str(pronouns[0])
    her_pronoun = str(pronouns[1])

    if her_pronoun == "them":
        her_pronoun = "their"

    time.sleep(0.5)

    your_day = input(f'''

Can't think of anything? Don't want to answer? 

Have one on me, and just enter 'x'!

What kind of day are you having today, {your_name}?: ''').lower()

    if your_day == "x" or " ":
        your_day = random.choice(your_day_x)

    time.sleep(0.5)

    favourite_place = input("Your favourite place in the world is... ").lower()

    if favourite_place == "x" or " ":
        favourite_place = random.choice(favourite_place_x)

    if favourite_place.find("my"):
        favourite_place = favourite_place.replace("my", her_pronoun)

    time.sleep(0.5)

    favourite_person = input("Your favourite person in the whole wide world is... ").title()

    if favourite_person == "X" or " ":
        favourite_person = random.choice(favourite_person_x)

    if favourite_person.find("My"):
        favourite_person = favourite_person.replace("My", her_pronoun)

    time.sleep(0.5)

    something_scary = input("You would hate it if you walked into a room and saw a thousand... ").lower()

    if something_scary == "x" or " ":
        something_scary = random.choice(something_scary_x)

    time.sleep(0.5)

    time_of_day = input("Your least favourite time of day is... ").lower()

    if time_of_day == "x" or " ":
        time_of_day = random.choice(time_of_day_x)

    if time_of_day.find("time") == -1:
        time_time_of_day = (time_of_day + ' time')
    else:
        time_time_of_day = time_of_day

    time.sleep(0.5)

    animal = input("One animal you wouldn't want to meet in a dark alley would be a... ").lower()

    if animal == "x" or " ":
        animal = random.choice(animal_x)

    time.sleep(0.5)
    something_deep = input("The deepest thing you can think of is a... ").lower()

    if something_deep == "x" or " ":
        something_deep = random.choice(something_deep_x)


    madlibs = ['''
Here...''', "We...", "Go...",
        
f'''
{your_name} was having a perfectly {your_day} day. When {she_pronoun} decided to have
a wander over to {her_pronoun} favourite place in the world, {favourite_place}.''',

f'''
While there, they saw {favourite_person} making out with ...''',

f'''
Ha ha, just kidding!''',

f'''
{favourite_person} was having a perfectly innocent time - doing the appropriate activity for the location.''',
f'''
Until...''',

f'''
A frenzied mass of {something_scary} started raining down from the sky, summersaulting through the air
like leaves in an autumn wind. They came crashing to the ground, as innocent onlookers screamed
for deliverance from the plague that had been sent upon their heads. ''',

f'''
{your_name} jumped into action - immediately running away, abandoning {favourite_person} to fend for themselves
amidst the stampeed of feet and falling {something_scary}.''', 

f'''
So bad was the carnage of the falling {something_scary}, that {your_name} went racing out into the {time_time_of_day} gloom. 
{your_name} was displeased - {her_pronoun} famous dislike of {time_of_day} adding to the irritation of the {something_scary}
-based apocalypse that {she_pronoun} had found {her_pronoun}self embroiled in.''',

f'''
Shrounded in the appropriate amount of shadows for the time of day, {your_name} came across a wounded {animal}.''',

f'''
Dodging around the still falling {something_scary}, {your_name} heaved the {animal} over {her_pronoun}
shoulder - exerting the appropriate amount of effort for the task.''', 

f'''
The {animal} however, was not pleased. It wriggled and writhed in {her_pronoun} grip - as displeased with
the attention as {your_name} was by the ever looming {time_of_day}.''',

f'''
{your_name} pushed {her_pronoun} feelings aside and forged ahead. Triumphant, determined. Wrestling with the 
{animal} {she_pronoun} turned, searching for something - eyes scanning the {something_scary} covered streets,
brow furrowed in concentration.''',

f'''
As {favourite_person} shouted encouragement from the entrance of {favourite_place} - still
only a few steps away, {your_name} found what {she_pronoun} was looking for.''',

f'''
Dodging the last of the falling {something_scary}, and kicking aside those that lay strewn on the ground
around {her_pronoun}.''',

f'''
Smiling, {your_name} took the still struggling {animal} from {her_pronoun} shoulder.''',

f'''
And threw it into a {something_deep}.''',

'''
THE END :)
''']


    for madlib in madlibs:
        print(madlib)
        time.sleep(3)

    game_end = input('''Do you want to go again? y/n
    
    : ''').lower()
    if game_end == "n":
        print("OK then, bye!")
        time.sleep(3)
        break 
