RED = "\033[31m"
RESET = "\033[0m"

story = """
Your name is Ruth, your a grade 11 girl who went to get groceries for your family

You are at the Walmart, when she hears police sirens

A voice comes over the intercom:

"Attention Come out with your hands up Slowly!"

The store is silent

Turns out there was a shooter

A few seconds later, another announcement follows:

As scared as you are in the store, you try to get out of the store
Suddenly! the store door closes

"We are coming in, Drop your weapon!"

Five minutes later, the police are trying to enter the door but turns out its bulletproof

Then 3 shots fire, Pow! Pow! Pow!
That was a warning shot, but you still can not see the shooter

Then suddenly her phone rings, Its your mum

You quickly answer the phone and reduces the volume as low as she can, and before her mum could even speak, a loading-
sound from a gun, rings next to her ear, its the shooter

He asks you to give him the phone, and now you have 2 options


A : Give him the phone
OR
B : Run away as fast as you can
"""

print(story)

user_choice = input()
user_choice = user_choice.lower()

if user_choice == "a":
    story = """
    He shoots the phone right in front of you and forces you to the back of the store with the other shoppers
    You then meet an old elderly couple named Jim and Bethany, Jim explains to you, that they came there to go get 
    Bethany's seizure medicine, till they was forced to stay back there

    You can relate-

    Suddenly, Bethany starts violently shaking, she is seizing

    You try calming her down by keeping her still but to no avail, it didnt work

    But something orange and small catches your eye, Its Bethany's seizure medicine, but its by the pharmacy counter

    But the shooter has his back turned

    Now's your chance

    You quickly run to the counter, grab Bethany's medicine and on your way back you trip, the shooter notices you, and
    approaches you slowly, gun's drawn

    You have 2 options

    C : You try to tell him the situation with Bethany

    D : You try to sneak back through the aisles with Jim and leave Bethany behind
    """
    print(story)

    user_choice = input()
    user_choice = user_choice.lower()

    if user_choice == "c":
        story = """
        He approaches you with his gun drawn What do you do?

        E : Freeze under the shelf and stay completely silent

        F : Panic, bolt upright, and try to run away
        """
        print(story)

        user_choice = input()
        user_choice = user_choice.lower()

        if user_choice == "e":
            story = "The shooter walks past you. You save Bethany with the medicine. SWAT breaches, and you, Jim, Bethany, and surviving shoppers escape together!"
            print(story)
            exit()

        if user_choice == "f":
            story = f"The shooter shoots and {RED}kills you instantly{RESET}. Jim manages to wheel Bethany with the help of other shoppers through the back exit while the shooter is distracted"
            print(story)
            exit()

    if user_choice == "d":
        story = """
        You try to help Jim move toward the back loading dock. Another shopper is nearby
        What happens next?

        G : The other hidden shopper panics, screams out your location 

        H : You slip through the back loading-dock door, and escape together without making noise
        """
        print(story)

        user_choice = input()
        user_choice = user_choice.lower()

        if user_choice == "g":
            story = f"You are betrayed by the shopper, and the shooter {RED}kills you execution-style{RESET} while the shopper survives"
            print(story)
            exit()

        if user_choice == "h":
            story = f"You, Jim, and Bethany, and others escape together into the parking lot! However, a slow shopper gets caught in the crossfire and {RED}dies{RESET}"
            print(story)
            exit()

if user_choice == "b":
    story = f"""
   You run as fast as you can and then you feel a sharp pain in your leg

   You fall, but your smart enough to dodge, and hide behind a shelf 

   You know you cant stay there for so long

   You have 2 options

   R : Use all your energy to the nearest exit (the pharmacy exit door)

   S : Surrender
    """
    print(story)

    user_choice = input()
    user_choice = user_choice.lower()

    if user_choice == "r":
        story = """
        You reach the pharmacy exit door, but it is jammed tight, but the shooters nearby
        What do you do?

        T : Smash the glass fire-alarm box next to the door to force the automatic locks open

        U : Hide in a nearby storage locker instead
        """
        print(story)

        user_choice = input()
        user_choice = user_choice.lower()

        if user_choice == "t":
            f"You somehow escape"
            print(story)
            exit()

        if user_choice == "u":
            story = f"You lock yourself in the locker. The shooter finds it, forces it open, and {RED}executes you{RESET}. No one escapes"
            print(story)
            exit()

    if user_choice == "s":
        story = """
        You surrender and the shooter captures you alive, using you as a human shield
        Police finally storm the store! What do you do?

        V : Try to trip the shooter in the chaos to help the police

        W : Obey the shooter completely and stay still to save your own skin
        """
        print(story)

        user_choice = input()
        user_choice = user_choice.lower()

        if user_choice == "v":
            story = f"Police breach and you trip him. You escape safely, but a stray bullet hits a hostage who {RED}dies{RESET} in the crossfire"
            print(story)
            exit()

        if user_choice == "w":
            story = f"You stay completely still. During the final SWAT raid, a stray bullet {RED}kills you{RESET}, and the shooter is finally arrested"
            print(story)
            exit()