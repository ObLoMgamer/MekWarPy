# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

class Equipment: #there will be an internal dict of all equipment
    def __init__(self):
        self.name="None"
        self.altNames=[]
        self.criticals=0
        self.tonnage=0
        self.bv=0
        self.cost=0
        self.rulesRef="None"
        self.description="None"


class Weapon(Equipment): #there will be an internal dict of all weapons
    def __init__(self):
        self.name = "None"
        self.altNames = [] #list of alternative lookup names
        self.tonnage = 0
        self.criticals = 0
        self.spreadable = False
        self.heat = 0
        self.damage = 0
        self.minimumRange = 0
        self.shortRange = 0
        self.mediumRange = 0
        self.longRange = 0
        self.extremeRange = 0
        self.bv = 0
        self.cost = 0
        self.rulesRefs = "None"
        self.description=""
        self.toHitModifier = 0
        self.ammoType = None

