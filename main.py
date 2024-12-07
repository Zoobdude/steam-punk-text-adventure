import json
import sys
import time
import os

mssgs = json.load(open("messages.json"))
robot = json.load(open("robot.json"))


def type(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def delete_last_x_lines(lines):
    for _ in range(lines):
        # Move the cursor up one line
        sys.stdout.write("\x1b[1A")
        # Clear the line
        sys.stdout.write("\x1b[2K")
    sys.stdout.flush()


def get_input(choices):
    user_input = input("\n >>> ")
    while user_input not in choices:
        print("Invalid input. Please try again.")
        time.sleep(1)
        delete_last_x_lines(2)
        user_input = input(">>> ")

    return user_input


def msg_wait():
    time.sleep(2)
    print()


def short_wait():
    time.sleep(1)
    print()

def the_end():
    #TODO
    
    print()
    print("THE END")

def title_output(message):
    os.system("clear")
    print(message)
    print()


def scene_1():
    type(mssgs["scene 1"])
    msg_wait()
    type(mssgs["scene 1 question"])

    match get_input(["1", "2", "3"]):
        case "1":  # short cut
            type(mssgs["scene 1.1"])
            msg_wait()
            type(mssgs["scene 1.1 question"])
            msg_wait()

            match get_input(["1", "2"]):
                case "1":  # run away
                    type(mssgs["scene 1.1.1"])

                case "2":  # fight
                    type(mssgs["scene 1.1.2"])
                    # loose two cog

        case "2":  # normal path
            type(mssgs["scene 1.2"])

        case "3":  # long path see bob
            type(mssgs["scene 1.3"])
            msg_wait()
            type(mssgs["scene 1.3 question"])
            choice3 = get_input(["1", "2"])

            match choice3:
                case "1":  # buy blueprints
                    type(mssgs["scene 1.3.1"])
                    # IMPLEMENT GAIN 1 BLUEPRINT

                case "2":  # decline
                    type(mssgs["scene 1.3.2"])

            msg_wait()

            type(mssgs["scene 1.3.2/1.3.1"])
            # IMPLEMENT LOOSE TWO COGS


def scene_2():
    type(mssgs["scene 2"])
    short_wait()
    type(mssgs["scene 2.0.1"])
    msg_wait()
    type(mssgs["scene 2 question"])

    match get_input(["1", "2", "3"]):
        case "1":  # first spot
            type(mssgs["scene 2.1"])
            short_wait()
            type(mssgs["scene 2.1.1"])

        case "2":  # second spot
            type(mssgs["scene 2.2"])
            short_wait()
            type(mssgs["scene 2.1.2"])

        case "3":  # third spot
            type(mssgs["scene 2.3"])
            short_wait()
            type(mssgs["scene 2.1.3"])

    msg_wait()

def scene_3():
    type(mssgs["scene 3"])
    msg_wait()
    
    type(mssgs["scene 3 question"])
    
    match get_input(["1", "2"]):
        case "1": #investigate trio
            type(mssgs["scene 3.0.1"])
            short_wait()
            type(mssgs["scene 3.0.1.1"])
            short_wait()
            type(mssgs["scene 3.0.1.2"])
            msg_wait()
            
            type(mssgs["scene 3.0.1 question"])
            
            match get_input(["1", "2"]):
                case "1": #investigate and run into enforcers
                    type(mssgs["scene 3.0.2.1"])
                    short_wait()
                    type(mssgs["scene 3.0.2.1.1"])
                    msg_wait()
                    print()
                    type("YOU DIED")
                    the_end()
                    
                case "2": #run back to street
                    type(mssgs["scene 3.0.2.2"])
                    short_wait()
                    type(mssgs["scene 3.0.2.2.1"])
                    short_wait()
                    type(mssgs["scene 3.0.2.2.2"])
                    short_wait()
                    type(mssgs["scene 3.1.1.1"])
                    short_wait()
                    type(mssgs["scene 3.1.1.3"])
                    
        case "2": #ignored the trio
            type(mssgs["scene 3.0.3.1"])
    
    msg_wait()
    type(mssgs["scene 3.1.1.2"])

def main():
    title_output(mssgs["Welcome Screen"])

    #scene_1()
    
    #TODO, implement random part picking for scene 2
    #scene_2()
    scene_3()


if __name__ == "__main__":
    main()
