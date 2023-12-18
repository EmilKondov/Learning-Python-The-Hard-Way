def golden_room():
    print("Welcome to heaven")
    print("How much gold do you want?")
    quantity = int(input())

    if quantity > 1000:
        print("Greedy bastard that is too much so you go to hell")
        dead()
    elif quantity < 1000 and quantity != 0:
        print("Go ahead and take it")
        print("You are now rich... this is the end of the game for you")
        exit(0)
    else:
        print("You are too shy ... c'mon try again")
        start()


def dead(why):
    print(why, "Good job!")
    exit(0)


def bear_room():
    print("Unfortunately you are in another dark room")
    print("This time there is a hungry bear")
    print("Decide your destiny now!!!")
    print("How are you going to deal with this bear?")
    bear_moved = False

    while True:
        choice = input("""
        > take honey
        > taunt bear
        > open door
        """)

        if choice == "take honey":
            dead("The bear ripped your head off because you took her honey")
        elif choice == "taunt bear" and not bear_moved:
            print('The bear moved from the door')
            print("You can go now")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear is not letting you second time, she chew off your legs")
        elif choice == "open door" and bear_moved:
            golden_room()
        else:
            print("I got no idea what that means.")

def narnia():
    print("""
    Welcome to the wonderland of Narnia!
    You need to choose if you like to help the Lion or not.
    """)

    answer = input("Would you help? ")

    if answer == "no":
        print("I am sorry... now you will disapear forever for not helping me")
    else:
        print("""
        Thank you for helping me! Now I will bring you back in your world
        and you can continue your journey.
        """)
        start()



def start():
    print("""
    You are in a drak room.
    There are two doors, left and right!
    You have to choose one!
    """)

    door = input("Choose your door wiseley: ")

    if door == "right":
        narnia()
    elif door == "left":
        bear_room()
    else:
        start()

start()
