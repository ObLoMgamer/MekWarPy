# This Python file uses the following encoding: utf-8
from app.core.Unit import *
from app.core.Player import *
#Mock up data and responses from server. We will use GCP Cloud Function with a database behind it for this

def getPlayerDataMock(playerID):
    #retrieve player by ID, whatever that will be, we won't need any other indeitifers initially. Let's mock up a hangar for this player
    #this function will just get the very basic player info

    #our entire hangar consisting of mechs, vehicles and infantry (each of those is dict of objects sorted by weight class)
    playerLogo = "" #img URL (s3 bucket or similar)
    elo = None #set player ELO to default, remember, this is client-side, so will take all info from sever anyway via either sockets or get/set methods
    faction = None #will be set from server, facion this player belongs to
    cbills = None
    intel = None
    reputation = None

def getPlayerHangarMock(playerID):
    #get the player's hangar and return it

    hangar = {'Mechs':{'Light':{}, 'Medium':{}, 'Heavy':{}, 'Assault':{}},
    'Vehicles':{'Light':{}, 'Medium':{}, 'Heavy':{}, 'Assault':{}},
    'Infantry': {'Light':{}, 'Medium':{}, 'Heavy':{}, 'Assault':{}}}

def getPlayerRosterMock(PlayerID):
     #get the player's roster of pilots/drivers and return it
     mwRoster = [] #roster of mechwarriors
     pilotRoster = [] #roster of vehicle pilots

def getPlayerMatchhistory(PlayerID):
     matchHistory = [] #chronological match history

#get player info
#send setters based on player interactions/commands

#get battle and matchmaking info
#get world state info
#get chat/message info

