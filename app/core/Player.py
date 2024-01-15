#Player class, everything the player needs to play the game on the client side

# This Python file uses the following encoding: utf-8
import sys,os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.core.Utils import *
from app.core.Unit import *

class Player:
        hangar = {'Mechs':[], 'Vehicles':[],'Infantry': []} #our entire hangar consisting of mechs, vehicles and infantry (each of those is dict of objects sorted by weight class)
	
        roster = {'MechWarriors':[], 'Pilots':[]} #inf platoons have in-built gunnery/piloting, and cannot be swapped

        playerLogo = None #img logo for the player, should be an S3 URL
        elo = None #set player ELO to default, remember, this is client-side, so will take all info from sever anyway via either sockets or get/set methods
        matchHistory = [] #chronological match history
        faction = None #will be set from server, facion this player belongs to
        factionReputation = {} #reputation for each relevant faction
        cbills = None
        intel = None
        reputation = None
        matchHistory = []

        def __init__(self, username):
            self.username = username

        def setHangar(self, hangar): #take a dict, and create an object for each item and store in the hangar

            for unitType in hangar:
                for unit in hangar[unitType]:
                    if unitType == 'Mechs':
                        unit = Mech(unit)
                    elif unitType == 'Vehicles':
                        unit = Vehicle(unit)
                    elif unitType == 'Infantry':
                        unit = Infantry(unit)
                    self.hangar[unitType].append(unit)

        def generateTestPilots(self):

            #if there are units to do this for
            for mech in self.hangar['Mechs']:
                #generate a mecharrior
                self.roster['MechWarriors'].append(Pilot('MechWarriors'))
            for vee in self.hangar['Vehicles']:
                self.roster['Pilots'].append(Pilot('Pilots'))
