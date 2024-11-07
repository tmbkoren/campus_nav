campusMap_nodes = {
    "Nutwood_Parking_Structure": (1170, 730, True),
    # "Eastside Parking Structure": (),
    # "State College Parking Structure": (),
    # "Parking Lot A": (),
    # "Parking Lot A(south)": {},
    # "Parking Lot C(east)": {},
    # "Parking Lot C(west)": {},
    # "Parking Lot E": {},
    # "ParkingPollak Library Lot G": {},
    # "Parking Lot F": {},
    # "Parking Lot I": {},
    # "Parking Lot R": {},
    "Titan_Shops": (840, 565, True),
    "Clayes_Performing_Arts_Center": (1000, 565, True),
    # "Titan_Gym": {},
    # "Titan_Sports Fields": {},
    # "Student_Recreation Center": {},
    "Titan_Student_Union": (850, 700, True),
    # "Langsdorf Hall": {},
    "McCarthy_Hall": (1100, 440, True),
    "Humanities_Building": (1005, 300, True),
    "Pollak_Library": (880, 420, True),
    # "Gordon Hall": {},
    # "KHS Building": {},

}

intersection_nodes = {
    "Nutwood_Upper": (1170, 640, False),
    "Nutwood_Upper_Left": (1065, 640, False),
    "Nutwood_Upper_Left_2": (1065, 653, False),

    "PLN_Upper": (880, 380, False),
    "PLN_Lower": (880, 457, False),
    "PLN_Lower_Right": (937, 457, False),
    "PLN_Lower_Right_Right": (957, 457, False),
    "PLN_Right": (957, 420, False),
    "PLN_Upper_Right": (957, 380, False),

    "TSU_Upper": (880, 625, False),
    "TSU_Right_1": (917, 625, False),
    "TSU_Right_1_Right": (937, 625, False),
    "TSU_Right_2": (917, 653, False),
    "TSU_Right_2_Right": (937, 653, False),

    "MH_Upper": (1100, 380, False),
    "MH_Upper_Left": (1065, 380, False),
    "MH_Left": (1065, 420, False),
    "MH_Left_2": (1065, 457, False),

    "Shop_Right": (865, 565, False),
    "Shop_Intersection": (880, 565, False),
    "Shop_Intersection_2": (937, 480, False),

    "CPAC_Left": (937, 590, False),

    "Hum_Lower": (1005, 340, False),
    "Hum_Lower_2": (1005, 380, False),
}

edges = {
    ("Nutwood_Parking_Structure", "Nutwood_Upper", 1),
    ("Nutwood_Upper", "Nutwood_Upper_Left", 1),
    ("Nutwood_Upper_Left", "Nutwood_Upper_Left_2", 1),
    ("Nutwood_Upper_Left_2", "TSU_Right_2_Right", 1),
    ("Nutwood_Upper_Left", "MH_Left_2", 1),

    ("McCarthy_Hall", "MH_Upper", 1),
    ("McCarthy_Hall", "MH_Left_2", 1),
    ("MH_Upper", "MH_Upper_Left", 1),
    ("MH_Left", "MH_Upper_Left", 1),
    ("MH_Left", "MH_Left_2", 1),
    ("MH_Left", "PLN_Right", 1),
    ("MH_Left_2", "PLN_Lower_Right_Right", 1),

    ("Pollak_Library", "PLN_Upper", 1),
    ("Pollak_Library", "PLN_Lower", 1),
    ("Pollak_Library", "PLN_Right", 1),
    ("PLN_Upper", "PLN_Upper_Right", 1),
    ("PLN_Upper_Right", "PLN_Right", 1),
    ("PLN_Lower", "PLN_Lower_Right", 1),
    ("PLN_Lower_Right", "PLN_Lower_Right_Right", 1),
    ("PLN_Lower_Right_Right", "PLN_Right", 1),
    ("PLN_Upper_Right", "Hum_Lower_2", 1),

    ("Titan_Student_Union", "TSU_Right_1", 1),
    ("Titan_Student_Union", "TSU_Right_2", 1),
    ("Titan_Student_Union", "TSU_Upper", 1),
    ("TSU_Upper", "TSU_Right_1", 1),
    ("TSU_Right_1", "TSU_Right_1_Right", 1),
    ("TSU_Right_1_Right", "TSU_Right_2_Right", 1),
    ("TSU_Right_1", "TSU_Right_2", 1),
    ("TSU_Right_2", "TSU_Right_2_Right", 1),

    ("Titan_Shops", "Shop_Right", 1),
    ("Shop_Intersection", "Shop_Right", 1),
    ("Shop_Intersection", "Shop_Intersection_2", 1),
    ("Shop_Intersection", "CPAC_Left", 1),
    ("Shop_Intersection", "PLN_Lower", 1),
    ("Shop_Intersection", "TSU_Upper", 1),
    ("Shop_Intersection_2", "PLN_Lower_Right", 1),
    ("Shop_Intersection_2", "PLN_Lower_Right_Right", 1),
    ("Shop_Intersection_2", "CPAC_Left", 1),

    ("Clayes_Performing_Arts_Center", "CPAC_Left", 1),
    ("CPAC_Left", "TSU_Right_1_Right", 1),

    ("Humanities_Building", "Hum_Lower", 1),
    ("Hum_Lower", "Hum_Lower_2", 1),
    ("Hum_Lower_2", "MH_Upper_Left", 1)
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