import time
import random
import pyfiglet


def sleep_time(target):
    print(target)
    time.sleep(3)


def time_faster(target):
    print(target)
    time.sleep(1)


def health_status(health_count):
    print(f"** HEALTH STATUS: {health_count} **\n")


def banner():
    ascii_banner = pyfiglet.figlet_format("Harry Potter and the",
                                          font="mini") \
                   + pyfiglet.figlet_format("The Philosopher's Stone",
                                            font="mini")
    print(ascii_banner)


def introduction(health_count):
    sleep_time("Mysterious letters begin arriving for Harry. ")
    sleep_time("At midnight, they hear a large bang on the "
               "door and Hagrid enters. ")
    sleep_time("Hagrid hands Harry an admissions letter to "
               "the Hogwarts School of Witchcraft and Wizardry. ")
    sleep_time("Harry arrives at Hogwarts and starts his first "
               "school year as a wizard. ")
    sleep_time("As the school year gets underway, "
               "Harry soon discovers his fate…\n")
    health_status(health_count)


def validate_input(input_value):
    while True:
        result = input(input_value)
        if result == '1':
            break
        elif result == '2':
            break
        elif result == '3':
            break
        else:
            time_faster("I don't understand your selection, please try again.")
    return result


def validate_play_input(string):
    while True:
        value_result = input(string).lower()
        if value_result == 'y':
            break
        elif value_result == 'n':
            break
        else:
            time_faster("I don't understand your selection, please try again.")
    return value_result


def game_over():
    time_faster("GAME OVER!!\n")


def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        time_faster("\n\nExcellent! Restarting the game ...\n\n")
        play_game()
    elif again == "n":
        time_faster("\n\nThanks for playing! See you next time.\n\n")
    else:
        play_again()


def detention(health_count):
    time_faster("WARNING: You have lost health points.\n")
    health_count -= 2
    health_status(health_count)
    if health_count == 0:
        time_faster("WARNING: You have run out of health points.\n")
        game_over()
    return health_count


def head_back(magical_items, health_count):
    time_faster("<--- HEADING BACK --->\n")
    move_around(magical_items, health_count)


def receive_parcel():
    sleep_time("Harry receives an invisibility cloak "
               "from an anonymous source claiming that the cloak "
               "belonged to Harry's father.\n")
    time_faster("DISCOVERED: Invisibility Cloak\n")


def die_roll_value():
    return random.randint(1, 6)


def dice_six():
    sleep_time("Face Quirinus Quirrell, "
               "the Defence Against the Dark Arts teacher.\n")
    final_chapter()


def consequence():
    return random.choice(['A massive mountain troll is blocking the entrance.',
                          'You get caught in Devil\'s Snare, '
                          'but manage to escape with Hermione\'s '
                          'fire-making spell.',
                          'You managed to mount a broom and '
                          'caught the correct key to open the door.',
                          'To get across the chamber, you checkmate '
                          'the King according to the rules of '
                          'Wizard\'s Chess.',
                          'You managed to solve the riddle and find the '
                          'potion that was safe to drink to allow onward '
                          'progress.'])


def final_chapter():
    time_faster("FINAL CHAPTER:\n")
    sleep_time("As Quirrell attempts to seize "
               "the stone and kill Harry, his flesh "
               "burns on contact with the boy's skin "
               "and breaks into blisters.")
    sleep_time("Harry's scar suddenly burns with pain "
               "and he passes out.")
    sleep_time("After three days you awake and have survived "
               "Voldemort and the stone has been destroyed.")
    sleep_time("The eventful school year ends at the final "
               "feast, during which Gryffindor wins the "
               "House Cup.\n")
    time_faster("YOU WIN!\n")
    play_again()


def roll_dice(magical_items, health_count):
    dice_value = die_roll_value()
    value = dice_value
    time_faster(f"You rolled a: {value}\n")
    choice = consequence()
    if value == 1 or value == 2 or value == 3 or value == 4:
        sleep_time(choice)
        time_faster("\n*ROLL DICE AGAIN*\n")
        roll_action(magical_items, health_count)
    elif value == 5:
        sleep_time("Unfortunately, you rolled a 5. This means detention.")
        detention(health_count)
        if health_count == 0:
            play_again()
        roll_dice(magical_items, health_count)
    elif value == 6:
        dice_six()


def roll_action(magical_items, health_count):
    enter = input("Press ENTER to roll:\n")
    if enter == '':
        roll_dice(magical_items, health_count)
    else:
        time_faster("Invalid selection.")
        roll_dice(magical_items, health_count)


def under_trapdoor(magical_items, health_count):
    sleep_time("You and your team encounter a "
               "series of obstacles, each of "
               "which requires unique skills, "
               "roll the dice:\n")
    sleep_time("You need to roll a 6 to move on.")
    roll_action(magical_items, health_count)


def explore(magical_items, health_count):
    sleep_time("You discover the Mirror of "
               "Erised, in which the viewer "
               "sees his or her deepest desires "
               "come true.")
    sleep_time("Harry is informed that the object "
               "kept under that trapdoor is a "
               "Philosopher's Stone, and Voldemort "
               "is plotting to steal it.\n")
    time_faster("Where would like to go to next:")
    explore_result = validate_input("1. Descend through the trapdoor\n"
                                    "2. Battle Voldemort\n")
    if explore_result == '1':
        under_trapdoor(magical_items, health_count)
    elif explore_result == '2':
        sleep_time("You are not strong enough to face Voldemort.")
        sleep_time("Voldemort got hold of the Philosopher's Stone.")
        sleep_time("He has returned to full power.\n")
        game_over()
        play_again()


def trophy_room(magical_items, health_count):
    if 'wand' not in magical_items:
        sleep_time("You arrive at the trophy room for the duel.")
        sleep_time("You hear footsteps and realize the duel was "
                   "a set-up by Malfoy to get you and Ron caught.\n")
        time_faster("You need to act fast. What is your next move?")
        trophy_selection = validate_input("1. Stay and face Filch, the "
                                          "school's caretaker.\n"
                                          "2. Escape to your dormitory.\n")
        if trophy_selection == '1':
            time_faster("You got caught, DETENTION.")
            detention_result = detention(health_count)
            health_count = detention_result

        elif trophy_selection == '2':
            if "wand" in magical_items:
                time_faster("NOTE: You have already found your "
                            "wand and managed to escape "
                            "without being caught.\n")
            else:
                time_faster("DISCOVERED: You managed to escape and "
                            "found your wand.\n")
                magical_items.append("wand")
    else:
        sleep_time("NOTE: You have already found your wand and managed "
                   "to escape without being caught.\n")

    if health_count == 0:
        play_again()
    else:
        head_back(magical_items, health_count)


def forbidden_corridor(magical_items, health_count):
    if 'trapdoor' in magical_items:
        time_faster("NOTE: You have already discovered the trapdoor."
                    "There is nothing else to do here.\n")
    else:
        if 'wand' in magical_items:
            sleep_time("You stumble into a room in a forbidden corridor.")
            sleep_time("A huge three-headed dog is standing "
                       "guard over a trapdoor.\n")
            time_faster("DISCOVERED: You have discovered the trapdoor.\n")
            time_faster("The parcel has arrived.\n")
            magical_items.append("trapdoor")
        else:
            sleep_time("NOTE: You need to face Malfoy "
                       "in the trophy room.\n")
    head_back(magical_items, health_count)


def awaiting_parcel(magical_items, health_count):
    if 'trapdoor' in magical_items:
        parcel_selection = validate_play_input("Would you like to use your "
                                               "cloak to investigate what is "
                                               "under the trapdoor? (y/n)\n")
        if parcel_selection == 'y':
            magical_items.append("cloak")
            explore(magical_items, health_count)
        elif parcel_selection == 'n':
            time_faster("Without the cloak you got caught "
                        "sneaking around after hours.")
            time_faster("You got caught, DETENTION.")
            item = detention(health_count)
            health_count = item

            if health_count == 0:
                play_again()
            else:
                head_back(magical_items, health_count)

    elif 'wand' not in magical_items:
        sleep_time("NOTE: Your parcel has not yet arrived.\n")
        head_back(magical_items, health_count)

    else:
        sleep_time("NOTE: You need go back and find the forbidden corridor.\n")
        head_back(magical_items, health_count)


def move_around(magical_items, health_count):
    time_faster("You are currently inside your "
                "dormitory at Hogwarts.")
    time_faster("Please enter the number of the "
                "room you would like to go to next:")
    selection = validate_input("1. Trophy Room\n"
                               "2. Forbidden Corridor\n"
                               "3. Receive parcel in dormitory\n")
    if selection == '1':
        trophy_room(magical_items, health_count)
    elif selection == '2':
        forbidden_corridor(magical_items, health_count)
    elif selection == '3':
        if 'trapdoor' in magical_items:
            receive_parcel()
        awaiting_parcel(magical_items, health_count)


def play_game():
    magical_items = []
    health_count = 6
    introduction(health_count)
    move_around(magical_items, health_count)


banner()
play_game()
