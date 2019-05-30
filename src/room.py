# Implement a class to hold room information. This should have name and
# description attributes.

import os

from id import setID
getID = setID()

class Room:
    def __init__(self, name, description="", connections=None, items=None, poi=None):
        self.id = f"r{getID()}"
        self.name = name
        self.description = description
        self.connections = connections
        self.items = items
        self.poi = poi
    def updateAttrs(self, attr, update):
        self[attr] = update
    def pickUpItem(self, temName):
        index = 0
        for i in range(0, len(items)):
            if(items[i].name is itemName):
                index = i
        return items.pop(index)
    def enter(self, playerName):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n{playerName} moves to the {self.name}.\n{self.description}")
    def connectRooms(self, roomID, toDirection):
        if self.connections is None:
            self.connections = {toDirection: roomID}
        else: 
            self.connections[toDirection] = roomID
