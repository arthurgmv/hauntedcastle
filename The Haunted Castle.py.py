print("Welcome to the Haunted Castle!")

current_room = "entryway"

while True:
    if current_room == "entryway":
        print("You are in the entryway of the castle.")
        print("You see a door to the north and a door to the east.")
        direction = input("Which direction would you like to go? [north, east] ").lower()
        if direction == "north":
            current_room = "dining room"
        elif direction == "east":
            current_room = "library"
        else:
            print("Invalid choice, try again.")
            
    elif current_room == "dining room":
        print("You are in the dining room.")
        print("There's a creepy portrait of a lady on the wall.")
        print("You hear a strange noise coming from the portrait.")
        action = input("What would you like to do? [investigate, leave] ").lower()
        if action == "investigate":
            print("As you approach the portrait, the lady comes to life!")
            print("She challenges you to a riddle:")
            print("I am light as a feather, yet even the strongest man cannot hold me for much longer than a minute.")
            answer = input("> ").lower()
            if answer == "breath":
                print("Correct! The lady returns to her portrait.")
                print("You can continue through the castle.")
                current_room = "entryway"
            else:
                print("Wrong answer. The lady curses you and you are trapped in the dining room forever.")
                break
        elif action == "leave":
            current_room = "entryway"
        else:
            print("Invalid choice, try again.")

    elif current_room == "library":
        print("You are in the library.")
        print("You see a mysterious book on the table.")
        print("You see a door to the west.")
        direction = input("Which direction would you like to go? [west, read book] ").lower()
        if direction == "west":
            current_room = "entryway"
        elif direction == "read book":
            print("As you open the book, a cloud of black smoke envelops you.")
            print("You are transported to the roof of the castle.")
            print("You have escaped the Haunted Castle!")
            fimA = input ("Press 'e' to leave (e)") 
            break
        else:
            print("Invalid choice, try again.")

