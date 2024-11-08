campusMap_nodes = {
    "Nutwood_Parking_Structure": (1170, 730, True),
    "Parking_Lot_F": (1000, 200, True),
    "ECS_Lawn": (800, 300, True),
    "ECS_Buildings": (785, 180, True),
    "Titan_Shops": (840, 565, True),
    "Clayes_Performing_Arts_Center": (1000, 565, True),
    "Titan_Gym": (700, 500, True),
    "Student_Recreation_Center": (700 ,700, True),
    "Titan_Student_Union": (850, 700, True),
    "Langsdorf_Hall": (1175, 350, True),
    "McCarthy_Hall": (1100, 440, True),
    "Humanities_Building": (1005, 300, True),
    "Pollak_Library": (880, 420, True),
    "EC_Building": (905, 310, True),
    "Gordon_Hall": (1095, 300, True),
    "KHS_Building": (740, 500, True),
    "Sports_Fields": (505, 442, True),

}

intersection_nodes = {
    "Nutwood_Upper": (1170, 640, False),
    "Nutwood_Upper_Left": (1065, 640, False),
    "Nutwood_Upper_Left_2": (1065, 653, False),

    "LotF_Entry": (955, 230, False),

    "ECS_Lawn_Right": (840, 310, False),
    "ECS_Lawn_Upper_Left": (760, 240, False),
    "ECS_Lawn_Lower_Left": (760, 340, False),

    "ECS_Lower_Right": (815, 220, False),
    "ECS_Right": (815, 180, False),
    "ECS_Upper_Right": (815, 130, False),
    "ECS_Lower_Left": (760, 220, False),
    "ECS_Left": (760, 180, False),
    "ECS_Upper_Left": (760, 130, False),

    "PLN_Upper": (880, 380, False),
    "PLN_Lower": (880, 457, False),
    "PLN_Lower_Right": (937, 457, False),
    "PLN_Lower_Right_Right": (957, 457, False),
    "PLN_Lower_Left": (750 ,457, False),
    "PLN_Right": (957, 420, False),
    "PLN_Upper_Right": (957, 380, False),
    "PLN_Upper_Left": (850, 357, False),

    "TSU_Upper": (880, 625, False),
    "TSU_Right_1": (917, 625, False),
    "TSU_Right_1_Right": (937, 625, False),
    "TSU_Right_2": (917, 653, False),
    "TSU_Right_2_Right": (937, 653, False),
    "TSU_Upper_Left": (805, 625, False),

    "MH_Upper": (1100, 380, False),
    "MH_Upper_Left": (1065, 380, False),
    "MH_Upper_Right": (1140, 380, False),
    "MH_Lower_Right": (1140, 555, False),
    "MH_Lower_Left": (1065, 555, False),
    "MH_Left": (1065, 420, False),
    "MH_Left_2": (1065, 457, False),
    "MH_Right": (1120, 435, False),
    "MH_Right_2": (1140, 435, False),

    "Shop_Right": (865, 565, False),
    "Shop_Left": (805, 560, False),
    "Shop_Intersection": (880, 565, False),
    "Shop_Intersection_2": (937, 480, False),

    "CPAC_Left": (937, 590, False),
    "CPAC_Upper": (1020, 488, False),
    "CPAC_Upper_Intersection": (1020, 457, False),

    "Hum_Lower": (1005, 340, False),
    "Hum_Lower_2": (1005, 380, False),
    "Hum_Left": (990, 310, False),
    "Hum_Right": (1030, 305, False),
    "Hum_GH_Junction": (1050, 330, False),

    "SRC_Entrance": (720, 610, False),
    "SRC_Right": (750, 610, False),

    "EC_Right_Entrance": (930, 330, False),
    "EC_Right_Intersection": (955, 330, False),
    "EC_Left_Entrance": (855, 330, False),

    "GH_Lower_Right": (1140, 315, False),

    "TG_Lower": (700, 530, False),
    "TG_Lower_Intersection": (700, 560, False),

    "KHS_Lower": (740, 530, False),
    "KHS_Lower_Intersection": (750, 560, False),
    "KHS_Right": (780, 500, False),

    "LH_Left_Entrance": (1140, 350, False),


    "GymDR_1": (640, 610, False),
    "GymDR_2": (640, 560, False),
    "GymDR_3": (640, 442, False),
    "GymDR_4": (640, 340, False),
    "GymDR_5": (640, 265, False),
}

edges = {
    ("Nutwood_Parking_Structure", "Nutwood_Upper", 276),
    ("Nutwood_Upper", "Nutwood_Upper_Left", 299),
    ("Nutwood_Upper_Left", "Nutwood_Upper_Left_2", 29),
    ("Nutwood_Upper_Left_2", "TSU_Right_2_Right", 393),
    ("Nutwood_Upper_Left", "MH_Lower_Left", 278),

    ("Parking_Lot_F", "LotF_Entry", 70),
    ("LotF_Entry", "EC_Right_Intersection", 138),

    ("ECS_Lawn", "ECS_Lawn_Right", 55),
    ("ECS_Lawn", "ECS_Lawn_Upper_Left", 70),
    ("ECS_Lawn", "ECS_Lawn_Lower_Left", 70),
    ("ECS_Lawn_Upper_Left", "ECS_Lawn_Lower_Left", 120),
    ("ECS_Lawn_Upper_Left", "ECS_Lower_Left", 55),
    ("ECS_Lawn_Lower_Left", "PLN_Lower_Left", 70),
    ("ECS_Lawn_Lower_Left", "EC_Left_Entrance", 155),
    ("ECS_Lawn_Lower_Left", "GymDR_4", 250),
    ("ECS_Lawn_Upper_Left", "GymDR_5", 250),
    

    ("ECS_Buildings", "ECS_Right", 55),
    ("ECS_Buildings", "ECS_Left", 55),
    ("ECS_Right", "ECS_Upper_Right", 50),
    ("ECS_Right", "ECS_Lower_Right", 50),
    ("ECS_Left", "ECS_Upper_Left", 50),
    ("ECS_Left", "ECS_Lower_Left", 50),
    ("ECS_Upper_Left", "ECS_Upper_Right", 55),
    ("ECS_Lower_Left", "ECS_Lower_Right", 55),
    ("ECS_Lower_Right", "ECS_Lawn_Right", 155),

    ("McCarthy_Hall", "MH_Upper", 159),
    ("McCarthy_Hall", "MH_Left_2", 104),
    ("McCarthy_Hall", "MH_Right", 58),
    ("MH_Upper", "MH_Upper_Left", 92),
    ("MH_Upper", "MH_Upper_Right", 120),
    ("MH_Left", "MH_Upper_Left", 102),
    ("MH_Left", "MH_Left_2", 102),
    ("MH_Left_2", "MH_Lower_Left", 285),
    ("MH_Lower_Left", "MH_Lower_Right", 206),
    ("MH_Right", "MH_Right_2", 38),
    ("MH_Right_2", "MH_Upper_Right", 152),
    ("MH_Right_2", "MH_Lower_Right", 341),
    ("MH_Left", "PLN_Right", 354),
    ("MH_Left_2", "CPAC_Upper_Intersection", 154),
    ("MH_Upper_Left", "Hum_GH_Junction", 181),

    ("Pollak_Library", "PLN_Upper", 117),
    ("Pollak_Library", "PLN_Lower", 119),
    ("Pollak_Library", "PLN_Right", 234),
    ("PLN_Upper", "PLN_Upper_Right", 234),
    ("PLN_Upper", "PLN_Upper_Left", 107),
    ("PLN_Upper_Right", "PLN_Right", 117),
    ("PLN_Lower", "PLN_Lower_Right", 234),
    ("PLN_Lower_Right", "PLN_Lower_Right_Right", 52),
    ("PLN_Lower", "PLN_Lower_Left", 200),
    ("PLN_Lower_Right_Right", "PLN_Right", 119),
    ("PLN_Upper_Left", "EC_Left_Entrance", 70),
    ("PLN_Lower_Right_Right", "CPAC_Upper_Intersection", 192),
    ("PLN_Upper_Right", "Hum_Lower_2", 153),
    ("PLN_Lower_Left", "KHS_Right", 138),

    ("Titan_Student_Union", "TSU_Right_1", 318),
    ("Titan_Student_Union", "TSU_Right_2", 253),
    ("Titan_Student_Union", "TSU_Upper", 272),
    ("TSU_Upper", "TSU_Right_1", 103),
    ("TSU_Upper", "TSU_Upper_Left", 210),
    ("TSU_Right_1", "TSU_Right_1_Right", 80),
    ("TSU_Right_1_Right", "TSU_Right_2_Right", 90),
    ("TSU_Right_1", "TSU_Right_2", 90),
    ("TSU_Right_2", "TSU_Right_2_Right", 80),

    ("Titan_Shops", "Shop_Right",  61),
    ("Titan_Shops", "Shop_Left", 94),
    ("Shop_Intersection", "Shop_Right", 48),
    ("Shop_Intersection", "Shop_Intersection_2", 281),
    ("Shop_Intersection", "CPAC_Left", 214),
    ("Shop_Intersection", "PLN_Lower", 313),
    ("Shop_Intersection", "TSU_Upper", 175),
    ("Shop_Intersection_2", "PLN_Lower_Right", 53),
    ("Shop_Intersection_2", "PLN_Lower_Right_Right", 73),
    ("Shop_Intersection_2", "CPAC_Left", 406),

    ("Clayes_Performing_Arts_Center", "CPAC_Left", 204),
    ("Clayes_Performing_Arts_Center", "CPAC_Upper", 247),
    ("CPAC_Upper", "CPAC_Upper_Intersection", 82),
    ("CPAC_Left", "TSU_Right_1_Right", 52),

    ("Humanities_Building", "Hum_Lower", 92),
    ("Humanities_Building", "Hum_Left", 45),
    ("Humanities_Building", "Hum_Right", 67),
    ("Hum_Right", "Hum_GH_Junction", 113),
    ("Hum_Lower", "Hum_Lower_2", 121),
    ("Hum_GH_Junction", "Gordon_Hall", 95),
    ("Hum_Lower_2", "MH_Upper_Left", 193),

    ("Student_Recreation_Center", "SRC_Entrance", 240),
    ("SRC_Entrance", "SRC_Right", 87),
    ("SRC_Right", "TSU_Upper_Left", 170),
    ("SRC_Entrance", "GymDR_1", 248),

    ("EC_Building", "EC_Right_Entrance", 79),
    ("EC_Building", "EC_Left_Entrance", 82),
    ("EC_Right_Entrance", "EC_Right_Intersection", 82),
    ("EC_Left_Entrance", "ECS_Lawn_Right", 55),
    ("EC_Right_Intersection", "PLN_Upper_Right", 188),
    ("EC_Right_Intersection", "Hum_Left", 134),

    ("Gordon_Hall", "GH_Lower_Right", 144),

    ("Titan_Gym", "TG_Lower", 94),
    ("TG_Lower", "TG_Lower_Intersection", 89),
    ("TG_Lower_Intersection", "GymDR_2", 159),

    ("KHS_Building", "KHS_Lower", 110),
    ("KHS_Lower", "KHS_Lower_Intersection", 101),
    ("KHS_Right", "KHS_Lower_Intersection", 138),
    ("KHS_Lower_Intersection", "TG_Lower_Intersection", 167),
    ("KHS_Lower_Intersection", "Shop_Left", 138),
    ("KHS_Lower_Intersection", "SRC_Right", 150),

    ("Langsdorf_Hall", "LH_Left_Entrance", 103),
    ("LH_Left_Entrance", "GH_Lower_Right", 105),
    ("LH_Left_Entrance", "MH_Upper_Right", 110),

    ("Sports_Fields", "GymDR_3", 405),

    ("GymDR_1", "GymDR_2", 188),
    ("GymDR_2", "GymDR_3", 356),
    ("GymDR_3", "GymDR_4", 295),
    ("GymDR_4", "GymDR_5", 219),
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