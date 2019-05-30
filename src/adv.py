from room import Room
from player import Player
from item import Item
from roomInfo import roomInfo


class Game:
    def __init__(self, roomsInfo, items=None):
        self.rooms = self._createRooms(roomsInfo)
        self.items = items

    def start(self):
        while True:
            print("Welcome to the game!  As of right now, you can walk around rooms but that's unfortunately it!\nEnter 'q' at any prompt to quit any time!")
            playerName = self._getPlayerName()
            if playerName == "q":
                break
            else:
                self.player = Player(playerName)
                self._enterRoom(self.player.location)
                break
                
    def _findRoomByID(self, id):
        for key in self.rooms:
            if self.rooms[key].id == id:
                return self.rooms[key]


    def _selectRoom(self, room):
        while True:
            direction = input(f"\nWhich direction would you like to go?  There are doorways in these directions:\n{', '.join(room.connections.keys())}: ")
            if direction == "q":
                break
            elif direction in room.connections:
                self._enterRoom(room.connections[direction])
                break

    def _enterRoom(self, roomID):
        self.player.location = roomID
        room = self._findRoomByID(roomID)
        room.enter(self.player.name)
        self._selectRoom(room)

    def _getPlayerName(self):
        playerName = input("\nPlease enter a name for your character: ")
        if len(playerName) > 0:
            return playerName

    def _linkRooms(self, rooms):
        for key in rooms:
            # Builds links for each room.  rooms[key] is the class object for a room.
            # The links are created from the provided links in roomInfo.
            # However, the connecting room's id must be found to create the connection
            links = roomInfo[key]["links"]
            for direction in links:
                linkedKey = links[direction]
                id = rooms[linkedKey].id
                rooms[key].connectRooms(id, direction)

    def _createRooms(self, roomsInfo):
        rooms = {}
        for key in roomInfo:
            # Iterate roomInfo and for each 'key', create a new Room class, populate 'rooms'
            info = roomInfo[key]
            rooms[key] = Room(info["name"], info["description"])
        # _linkRooms will mutate the objects, no need to assign
        self._linkRooms(rooms)
        return rooms
    

    
game = Game(roomInfo)
game.start()