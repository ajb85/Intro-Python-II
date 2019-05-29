# Write a class to hold player information, e.g. what room they are in
# currently.

from id import setID
getID = setID()

class Player:
    def __init__(self, name, location="r1", inventory=[]):
        self.id = f"p{getID()}"
        self.name = name
        self.location = location
        self.inventory = inventory
    def pickUpItem(id):
        self.inventory.append(id)
    def dropItem(id):
        self.inventory.remove(id)
    def moveToRoom(id):
        self.location = id