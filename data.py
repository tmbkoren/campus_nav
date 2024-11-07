campusMap_nodes = {
    "Nutwood Parking Structure": (1170, 730, True),
    # "Eastside Parking Structure": (),
    # "State College Parking Structure": (),
    # "Parking Lot A": (),
    # "Parking Lot A(south)": {},
    # "Parking Lot C(east)": {},
    # "Parking Lot C(west)": {},
    # "Parking Lot E": {},
    # "Parking Lot G": {},
    # "Parking Lot F": {},
    # "Parking Lot I": {},
    # "Parking Lot R": {},
    "Titan Shops": (840, 565, True),
    "Clayes Performing Arts Center": (1000, 565, True),
    # "Titan Gym": {},
    # "Titan Sports Fields": {},
    # "Student Recreation Center": {},
    "Titan Student Union": (850, 700, True),
    # "Langsdorf Hall": {},
    "McCarthy Hall": (1100, 440, True),
    "Humanities Building": (1005, 300, True),
    "Pollak Library": (880, 420, True),
    # "Gordon Hall": {},
    # "KHS Building": {},

}

intersection_nodes = {
    "Nutwood Upper": (1170, 640, False),
    "Nutwood Upper Left": (1065, 640, False),
    "Nutwood Upper Left 2": (1065, 653, False),

    "PLN Upper": (880, 380, False),
    "PLN Lower": (880, 457, False),
    "PLN Lower Right": (937, 457, False),
    "PLN Lower Right Right": (957, 457, False),
    "PLN Right": (957, 420, False),
    "PLN Upper Right": (957, 380, False),

    "TSU Upper": (880, 625, False),
    "TSU Right 1": (917, 625, False),
    "TSU Right 1 Right": (937, 625, False),
    "TSU Right 2": (917, 653, False),
    "TSU Right 2 Right": (937, 653, False),

    "MH Upper": (1100, 380, False),
    "MH Upper Left": (1065, 380, False),
    "MH Left": (1065, 420, False),
    "MH Left 2": (1065, 457, False),

    "Shop Right": (865, 565, False),
    "Shop Intersection": (880, 565, False),
    "Shop Intersection 2": (937, 480, False),

    "CPAC Left": (937, 590, False),

    "Hum Lower": (1005, 340, False),
    "Hum Lower 2": (1005, 380, False),
}

edges = {
    ("Nutwood Parking Structure", "Nutwood Upper", 1),
    ("Nutwood Upper", "Nutwood Upper Left", 1),
    ("Nutwood Upper Left", "Nutwood Upper Left 2", 1),
    ("Nutwood Upper Left 2", "TSU Right 2 Right", 1),
    ("Nutwood Upper Left", "MH Left 2", 1),

    ("McCarthy Hall", "MH Upper", 1),
    ("McCarthy Hall", "MH Left 2", 1),
    ("MH Upper", "MH Upper Left", 1),
    ("MH Left", "MH Upper Left", 1),
    ("MH Left", "MH Left 2", 1),
    ("MH Left", "PLN Right", 1),
    ("MH Left 2", "PLN Lower Right Right", 1),

    ("Pollak Library", "PLN Upper", 1),
    ("Pollak Library", "PLN Lower", 1),
    ("Pollak Library", "PLN Right", 1),
    ("PLN Upper", "PLN Upper Right", 1),
    ("PLN Upper Right", "PLN Right", 1),
    ("PLN Lower", "PLN Lower Right", 1),
    ("PLN Lower Right", "PLN Lower Right Right", 1),
    ("PLN Lower Right Right", "PLN Right", 1),
    ("PLN Upper Right", "Hum Lower 2", 1),

    ("Titan Student Union", "TSU Right 1", 1),
    ("Titan Student Union", "TSU Right 2", 1),
    ("Titan Student Union", "TSU Upper", 1),
    ("TSU Upper", "TSU Right 1", 1),
    ("TSU Right 1", "TSU Right 1 Right", 1),
    ("TSU Right 1 Right", "TSU Right 2 Right", 1),
    ("TSU Right 1", "TSU Right 2", 1),
    ("TSU Right 2", "TSU Right 2 Right", 1),

    ("Titan Shops", "Shop Right", 1),
    ("Shop Intersection", "Shop Right", 1),
    ("Shop Intersection", "Shop Intersection 2", 1),
    ("Shop Intersection", "CPAC Left", 1),
    ("Shop Intersection", "PLN Lower", 1),
    ("Shop Intersection", "TSU Upper", 1),
    ("Shop Intersection 2", "PLN Lower Right", 1),
    ("Shop Intersection 2", "PLN Lower Right Right", 1),
    ("Shop Intersection 2", "CPAC Left", 1),

    ("Clayes Performing Arts Center", "CPAC Left", 1),
    ("CPAC Left", "TSU Right 1 Right", 1),

    ("Humanities Building", "Hum Lower", 1),
    ("Hum Lower", "Hum Lower 2", 1),
    ("Hum Lower 2", "MH Upper Left", 1)
}

def getCampusMap():
    return campusMap_nodes

def getIntersectionNodes():
    return intersection_nodes

def getEdges():
    return edges

def getHelpCoords():
    helpCoords = {}
    for x in range(0, 1281, 100):
        for y in range(0, 834, 100):
            helpCoords[(x, y)] = (x, y)
    return helpCoords