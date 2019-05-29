from room import Room
from player import Player
from item import Item
from roomInfo import roomInfo

# Declare all the rooms

class Game:
    def __init__(self, roomsInfo, items=[]):
        self.rooms = self._getRooms(roomsInfo)
        self.items = items

    def _findByID(self, collection, id):
        for thing in self[collection]:
            if thing.id is id:
                return thing

    def _linkRooms(self, rooms):
        for key in rooms:
            # Build links for each room.  rooms[key] is the class object for a room.
            # The links are created from the provided links in roomInfo.
            # However, the connecting room's id must be found to create the connection
            links = roomInfo[key]["links"]
            for direction in links:
                linkedKey = links[direction]
                id = rooms[linkedKey].id
                rooms[key].connectRooms(id, direction)

    def _getRooms(self, roomsInfo):
        rooms = {}
        for key in roomInfo:
            # Iterate roomInfo and for each 'key', create a new Room class, populate 'rooms'
            info = roomInfo[key]
            rooms[key] = Room(info["name"], info["description"])
        # _linkRooms will mutate the objects, no need to assign
        self._linkRooms(rooms)
        return rooms

    def commands(self, input):
        commands = {"q":False}
        if input in commands:
            return commands[input]
        else:
            return None
    
    def _getName(self):
        while True:
            input = Input("Please enter a name for your character: ")
            command = 
            if len(playerName) > 0:
                return playerName

    def start(self):
        while True:
            playerName = self._getName()
            self.player = Player(playerName)


    def exploreRoom(self, id):
        room = self._findByID("rooms", id)
        print("You look around the room, here's what you see: ")
        for item in room.items:
            print(item)
    
    def enterRoom(self, id):
        self.player.moveToRoom(id)
        room = self._findByID("rooms", id)
        print(room.description)


    
game = Game(roomInfo)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:``
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

