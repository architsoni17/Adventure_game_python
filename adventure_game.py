import time
import random


list1 = ["vampire", "pistol"]  # LIST CREATED TO TAKE ANY RANDOM OPTION
list2 = []  # EMPTY LIST TO STORE PISTOL WHEN IT IS FOUND


def restart():  # restarts from the introduction
    list2.clear()  # will clear all items appended in the list
    game()


def print_pause(stri, times):  # FUNCTION FOR DELAYING PRINTING VALUES
    print(stri)
    time.sleep(times)


def intro():  # FUNCTION FOR INTRODUCTION OPTION
    print_pause("Now we will start this adventure game", 2)
    print_pause("""Suppose you land in amusement park at midnight
you are warned that there is a vampire present in
this park due to which it is closed for many years""", 2)
    print_pause("""The way to kill that vampire is to find
a hidden gun in that park""", 2)
    print_pause("There are two options in front of you", 2)
    print_pause(""""Note:To restart the game type
    'R' and to exit type'E' anywhere""", 2)


def user_option1():  # FUNCTION FOR FIRST USER CHOICE BETWEEN TWO LOCATIONS
    print_pause("Where to go?", 2)
    print_pause("1. Enter into a candy shop present in front of you.", 2)
    print_pause("2. Enter into a shooting cabin", 2)
    user_option2()


def user_option2():  # FUNCTION FOR DESCRIBING SCENARIOS AT LOCATIONS
    choice2 = input("Enter your choice (1 or 2)").lower()
    if choice2 == '1':
        print_pause("You entered the candy shop!!", 2)
        user_option3()
    elif choice2 == '2':
        print_pause("You entered the shooting cabin!!", 2)
        user_option3()
    elif choice2 == 'r':
        restart()
    elif choice2 == 'e':
        print_pause("Thanks for playing!!", 2)
        exit()
    else:
        print_pause("Invalid input", 2)
        user_option1()


def user_option3():  # FUNCTION FOR MAIN GAME ENCOUNTER WITH VAMPIRE AND PISTOL
    scene1 = random.choice(list1)
    if scene1 == 'vampire':
        print_pause("Oh my god there is a vampire!!", 2)
        choice3 = input("""What to do now?
1.run
2.fight (1 or 2)""").lower()
        if choice3 == '1':
            print_pause("You decided to go back to the field!", 2)
            user_option1()
        elif choice3 == '2':
            if "pistol" in list2:
                print_pause("Hurray you killed the vampire!!  GAME OVER!!", 2)
            else:
                print_pause("""you got killed by vampire you were empty handed"
       GAME OVER!!""", 2)
        elif choice3 == 'r':
            restart()
        elif choice3 == 'e':
            print_pause("Thanks for playing!!", 2)
            exit()
        else:
            print("Wrong choice!!")
            user_option3()
    else:
        print_pause("hey you got a pistol well done you got the weapon!!", 2)
        list2.append("pistol")
        print_pause("Lets go back to field!!", 2)
        user_option1()


def game():
    choice1 = input("Would you like to play the adventure game? (yes,no)")
    if choice1.lower() == 'yes':
        intro()  # CALLING INTRO
        user_option1()  # CALLING FUNCTION user_option1
    elif choice1.lower() == 'no':
        print_pause(" ok come when you like to play!", 2)
    else:
        print_pause("Wrong choice!!", 2)
        game()


game()
