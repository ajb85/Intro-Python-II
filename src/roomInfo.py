roomInfo = {
    "outside":{
        "name": "Outside Cave Entrance", 
        "description": "North of you, the cave mount beckons", 
        "links":{"north":"foyer"} 
    },
    "foyer":{
        "name": "Foyer", 
        "description": "Dim light filters in from the south. Dusty passages run north and east.", 
        "links":{"south":"outside", "north":"overlook", "east":"narrow"}
    },
    "overlook":{
        "name": "Grand Overlook", 
        "description": """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", 
        "links":{"south":"foyer"}
    },
    "narrow":{
        "name": "Narrow Passage", 
        "description": """The narrow passage bends here from west to north. The smell of gold permeates the air.""", 
        "links":{"west":"foyer", "north":"treasure"}
    },
    "treasure":{
        "name": "Treasure Chamber", 
        "description": """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""", 
        "links":{"south":"narrow"}
    }
}