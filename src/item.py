from id import setID
getID = setID()

class Item:
    def __init__(self, name, description):
        self.id = f"i{getID()}"
        self.name = name
        self.description = description
    def examine():
        print(self.description)