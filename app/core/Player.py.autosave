#Player class, everything the player needs to play the game on the client side
class Player:
	hangar = {'Mechs':{'Light':{}, 'Medium':{}, 'Heavy':{}, 'Assault':{}}, 
	'Vehicles':{'Light':{}, 'Medium':{}, 'Heavy':{}, 'Assault':{}}, 
	'Infantry': {'Light':{}, 'Medium':{}, 'Heavy':{}, 'Assault':{}}} #our entire hangar consisting of mechs, vehicles and infantry (each of those is dict of objects sorted by weight class)
	
	mwRoster = [] #roster of mechwarriors
	pilotRoster = [] #roster of vehicle pilots

	playerLogo = None #img logo for the player
	elo = None #set player ELO to default, remember, this is client-side, so will take all info from sever anyway via either sockets or get/set methods
	matchHistory = [] #chronological match history
	faction = None #will be set from server, facion this player belongs to
	cbills = None
	intel = None
	reputation = None
	matchHistory = []


	def __init__(self, username):
		self.username = username