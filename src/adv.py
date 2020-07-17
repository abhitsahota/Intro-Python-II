from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 'outside'),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", 'foyer'),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", 'overlook'),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", 'narrow'),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", 'treasure'),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#


# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

p_name = input("What's your name?  ")
player = Player(p_name, room['outside'])
print(player)


def next_room(dir, current_room):
    print(current_room, dir, current_room.key)
    direction = dir + "_to"
    next_room = getattr(room[current_room.key], direction)
    print(next_room)
    return next_room

def move_player(ply, dir):
    room = next_room(dir, ply.current_room)
    if room:
        ply.current_room = room
        print(f"You move {dir} and find yourself somewhere new")
        return True
    else:
        return False

print(f"{p_name}, let's get started on your adventure. Type q to quit at anytime.\n")

selection = False
while not selection:
    print(f"{p_name}. You are {player.current_room.name}. {player.current_room.description}")
    command = input("Where would you like to go? Type n, e, s, or w to move.  ").lower()

    try:
        if command == 'q':
            selection = True
            break

        if command in ["n", "e", "s", "w"]:
            if move_player(player, command):
                continue
            else:
                print("There is no room that way, try another direction.")
                continue
        else: 
            print('Please enter a direction (n,e,s,w) or q to quit')
    except ValueError:
        print('Please enter a direction (n,e,s,w) or q to quit')