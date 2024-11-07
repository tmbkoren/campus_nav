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
    # "Titan Shops": (),
    # "Titan Gym": {},
    # "Titan Sports Fields": {},
    # "Student Recreation Center": {},
    "Titan Student Union": (850, 700, True),
    # "Langsdorf Hall": {},
    "McCarthy Hall": (1100, 440, True),
    # "Humanities Building": {},
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
    "TSU Right 1": (917, 625, False),
    "TSU Right 1 Right": (937, 625, False),
    "TSU Right 2": (917, 653, False),
    "TSU Right 2 Right": (937, 653, False),
    "MH Upper": (1100, 380, False),
    "MH Upper Left": (1065, 380, False),
    "MH Left": (1065, 420, False),
    "MH Left 2": (1065, 457, False),
}

edges = {
    ("Nutwood Parking Structure", "Nutwood Upper"),
    ("Nutwood Upper", "Nutwood Upper Left"),
    ("Nutwood Upper Left", "Nutwood Upper Left 2"),
    ("Nutwood Upper Left 2", "TSU Right 2 Right"),
    ("Nutwood Upper Left", "MH Left 2"),

    ("MH Left", "McCarthy Hall"),
    ("MH Upper", "McCarthy Hall"),
    ("MH Left", "MH Upper Left"),
    ("MH Left", "MH Left 2"),
    ("MH Left", "PLN Right"),
    ("MH Left 2", "PLN Lower Right Right"),

    ("Pollak Library", "PLN Upper"),
    ("Pollak Library", "PLN Lower"),
    ("Pollak Library", "PLN Right"),
    ("PLN Upper", "MH Upper"),
    ("PLN Lower", "PLN Lower Right"),
    ("PLN Lower Right", "PLN Lower Right Right"),
    ("PLN Lower Right Right", "PLN Right"),
    ("PLN Lower Right", "TSU Right 1 Right"),
    ("PLN Upper", "MH Upper"),

    ("Titan Student Union", "TSU Right 1"),
    ("Titan Student Union", "TSU Right 2"),
    ("TSU Right 1", "PLN Lower"),
    ("TSU Right 1", "TSU Right 1 Right"),
    ("TSU Right 1 Right", "TSU Right 2 Right"),
    ("TSU Right 1", "TSU Right 2"),
    ("TSU Right 2", "TSU Right 2 Right")
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