RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"


def main():
    """
    This runs the text based adventure
    This follows 10 rooms
    and has massive amounts of code
    :return: None
    """
    has_key = 0
    has_disguise = 0
    sleepy_stew = 0
    knows_code = 0
    key_stolen = 0
    problem = 0

    place = "cell"

    while True:
        if place == "cell":
            if has_key == 0:
                print("\nYour name is Jack. You are in a dungeon, trapped by the king's guards")
                print("You need to escape\n")
                print("There is a magnet in your pocket")
                print("Outside your cell door, there is a small key on the ground out of reach\n")
                print("A : Use the magnet in your pocket to pull the key through the bars")
                print("B : Try to reach the key with your hands")

                choice = input("  ").strip().lower()

                if choice == "b":
                    problem = 1
                    print(f"\nYour fingers touch the key. A guard hears you reaching through the bars and {RED}slaps your hand back{RESET} Try again")
                elif choice == "a":
                    has_key = 1
                    print(f"\nYou tie a loose thread to your magnet and toss it through the bars")
                    print(f"{GREEN}The key attaches to the magnet and you pull it into your cell{RESET}")
                    place = "corridor"
                else:
                    print(f"\n{RED} type one of the options ;-;{RESET}")

            if has_key == 1:
                print("\nLocation: Dungeon Cell")
                print("Your cell door is unlocked\n")
                print("A : Step out into the hallway")

                choice = input("  ").strip().lower()

                if choice == "a":
                    place = "corridor"
                else:
                    print(f"\n{RED} type one of the options ;-;{RESET}")

        elif place == "corridor":
            print("\nLocation: Dungeon Corridor")
            print("You step out into the hallway\n")
            print("A : Go down the vent")
            print("B : Go down the main Guard Corridor")

            choice = input("  ").strip().lower()

            if choice == "a":
                problem = 1
                print(f"\nYou crawl into the small vent, but it starts collapsing. {RED}You hurry back out before it gets more tight{RESET} Try another way")
            elif choice == "b":
                place = "guard corridor"
            else:
                print(f"\n{RED} type one of the options ;-;{RESET}")

        elif place == "guard corridor":
            print("\nLocation: Guard Corridor")
            print("You step into the Guard Corridor")
            print("You hear guards shouting further ahead\n")
            print("A : Duck into the Armory")
            print("B : Stand completely still and pretend to be a servant")

            choice = input("  ").strip().lower()

            if choice == "b":
                problem = 1
                print(f"\nThe guard looks at you suspiciously. {RED}You run away before he suspects you more{RESET} Pick a safer option")
            elif choice == "a":
                place = "armory"
            else:
                print(f"\n{RED} type one of the options ;-;{RESET}")

        elif place == "armory":
            has_disguise = 1
            print("\nLocation: Armory")
            print(f"{GREEN}You quickly put on a guard uniform as a disguise{RESET}")
            print("Armor is in the room\n")
            print("A : Walk to the Guard Post in your armor")
            print("B : Try to squeeze through a tiny supply chute in the back")

            choice = input("  ").strip().lower()

            if choice == "b":
                problem = 1
                print(f"\nYou start getting stuck in the narrow chute. {RED}You squeeze yourself back out before anyone sees you{RESET} Choose another route")
            elif choice == "a":
                place = "guard post"
            else:
                print(f"\n{RED} type one of the options ;-;{RESET}")

        elif place == "guard post":
            print("\nLocation: Guard Post")
            if has_disguise == 1:
                print("Wearing your guard disguise, you walk into the Guard Post")
                print("The guards nod at you and ignore you completely")
                print("You see a key resting on the Warden's desk nearby\n")
                print("A : Walk into the Kitchen")
                print("B : Stop to swipe the key from the desk")

            choice = input("  ").strip().lower()

            if choice == "b":
                key_stolen = 1
                problem = 1
                print(f"\nThe captain looks over at his desk. {RED}You snatch the key and pull your hand back just in time{RESET} Focus on escaping")
            elif choice == "a":
                place = "kitchen"
            else:
                print(f"\n{RED} type one of the options ;-;{RESET}")

        elif place == "kitchen":
            print("\nLocation: Kitchen")

            if sleepy_stew == 0:
                print("You step into the hot Kitchen. A giant pot of stew is bubbling over the fire")
                print("You see a jar of sleeping herbs on the counter\n")
                print("A : Dump the entire jar into the pot")
                print("B : Wait in the kitchen and eat a bowl of the spiked stew yourself cause your hungry")

                choice = input("  ").strip().lower()

                if choice == "b":
                    print(f"\nYou smell the sleeping herbs and realize eating it is a terrible idea. {RED}You put the bowl down{RESET} Choose another path")
                elif choice == "a":
                    sleepy_stew = 1
                    print(f"\n{GREEN}The Steam from the pot goes through the vent, and the guards are sleepy{RESET}")
                    place = "great hall"
                else:
                    print(f"\n{RED} type one of the options ;-;{RESET}")

            if sleepy_stew == 1:
                print("The pot of spiked stew is still bubbling\n")
                print("A : Walk into the Great Hall while the fumes work")

                choice = input("  ").strip().lower()

                if choice == "a":
                    place = "great hall"
                else:
                    print(f"\n{RED} type one of the options ;-;{RESET}")

        elif place == "great hall":
            print("\nLocation: Great Hall")

            if sleepy_stew == 0:
                print("You enter the Great Hall.")
                print("There are Guards eating.")
                print("You cannot pass through to the main gate\n")
                print("A : Head into the Kitchen to find a way to distract them")
                print("B : Try to run past the tables to the Exit")

                choice = input("  ").strip().lower()

                if choice == "b":
                    problem = 1
                    print(f"\nMultiple guards reach for their swords as you step forward. {RED}You back away quickly.{RESET} Find a better plan")
                elif choice == "a":
                    place = "kitchen"
                else:
                    print(f"\n{RED} type one of the options ;-;{RESET}")

            if sleepy_stew == 1:
                print("You hear all the guards in the Great Hall snoring loudly from the stew smokes")
                print("The path to the exit is completely clear\n")
                print("A : Walk into the Library")

                choice = input("  ").strip().lower()

                if choice == "a":
                    place = "library"
                else:
                    print(f"\n{RED} type one of the options ;-;{RESET}")

        elif place == "library":
            knows_code = 1
            print("\nLocation: Library")
            print("You enter the quiet Library. Theres a book")
            print("You read it carefully and the book asks what year was Taylor Swifts first album published")
            print("You dont think much about the book\n")
            print("A : Walk into the Pantry")
            print("B : Tear up the book and set fire to the library shelves")

            choice = input("  ").strip().lower()

            if choice == "b":
                problem = 1
                print(f"\nSetting a fire right now would ruin your chance to escape. {RED}Escape{RESET}")
            elif choice == "a":
                place = "pantry"
            else:
                print(f"\n{RED} type one of the options ;-;{RESET}")

        elif place == "pantry":
            print("\nLocation: Pantry")
            print("You walk into the Pantry filled with food barrels.")
            print("You hear all the guards in the Great Hall snoring loudly from the stew smokes.\n")

            if key_stolen == 1:
                print(f"{GREEN}You unlock a locked side door with the stolen master key{RESET}")

            print("A : Walk into the Exit Gatehouse")
            print("B : Hide inside an empty wine barrel")

            choice = input("  ").strip().lower()

            if choice == "b":
                print(f"\nYou climb into a barrel but realize you'll just get trapped. {RED}You climb back out{RESET} Go to the exit")
            elif choice == "a":
                place = "exit gatehouse"
            else:
                print(f"\n{RED} type one of the options ;-;{RESET}")

        elif place == "exit gatehouse":
            print("\nLocation: Exit Gatehouse")
            print("You reach the Exit Gatehouse. A wheel controls the bridge.")

            if knows_code == 1:
                print("A keypad requires the 4-digit passcode year you learned in the Library")

            

            print("Type the 4-digit year passcode into the keypad:")

            passcode = input("  ").strip().lower()

            if passcode == "2006":
                print(f"\n{GREEN}You spin the wheel and the exit bridge slams down.{RESET}")
                if problem == 1:
                    print(f"{YELLOW}Guards are running to your way, but you manage to run away{RESET}")
                print(f"{GREEN}You run to the forest to freedom. YOU ESCAPED AND WON{RESET}")
                break
            else:
                problem = 1
                print(f"\nThe keypad buzzes red. {RED}Incorrect passcode{RESET} Try entering the year again")

main()