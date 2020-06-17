#!/bin/python

#SETUP
import random
import time
import sys
characterlist = ""
deadinround = [] 
i = 0
srandom = random.SystemRandom()
class bcolors:
    Player = '\033[92m'
    DAY = '\033[94m\033[4m'
    RED = '\033[91m'
    USER = '\033[91m'
    oPlayer = '\033[95m'
    VOTE = '\033[91m'
    ENDC = '\033[0m'
    ENDCO = '\033[0m\033[0m'
    BOLD = '\033[1m'
    TITLE = '\033[92m\033[4m\033[1m'
    ENDTITLE = '\033[0m\033[0m'
    UNDERLINE = '\033[4m'


#GET LIST OF CHARACTERS:
autoinit = False
if len(sys.argv) > 1:
	arg = sys.argv[1]
	if arg == "auto":
		autoinit = True

if autoinit:
	amountPeople = 24
	characterlist = "Percy Jackson,Annabeth Chase,Jason Grace,Piper McLean,Frank Zhang,Hazel Levesque,Leo Valdez,Calypso,Grover Underwood,Tyson,Thalia Grace,Luke Castellan,Nico Di Angelo,Bianca Di Angelo,Clarisse La Rue,Silena Beauregard,Mr. D,Chiron,Rachel E. Dare,Zoe Nightshade,Reyna R.A,Hylla R.A,Octavian,Bastien"
else:
	amountPeople = int(input("How much characters?  "))
	while i<amountPeople:
		i += 1
		character = input("Name of character n"+str(i)+":  ")
		characterlist += ","+str(character)

#MAKE A LIST FROM LIST OF CHARACTERS
characterlist = characterlist[1:]
characterlist = characterlist.split(',')
aliveplayers = characterlist.copy()



def hunt(name,oplayer):
	playerc = bcolors.Player+name.strip()+bcolors.ENDC
	oplayerc = bcolors.oPlayer+oplayer.strip()+bcolors.ENDC
	hunted = ["food","rabbit",oplayerc,"doe","fish"]
	oindex = int(srandom.randrange(0, len(hunted)))
	hunteditem = hunted[oindex].strip()
	print(playerc,"hunted",hunteditem)



def hide(name, oplayer):
	playerc = bcolors.Player+name.strip()+bcolors.ENDC
	oplayerc = bcolors.oPlayer+oplayer.strip()+bcolors.ENDC
	hides = ["in the forest","in a tree","from "+oplayerc+"in a bush","in a bush","in a tree"]
	uindex = int(srandom.randrange(0, len(hides)))
	hidenin = hides[uindex].strip()
	print(playerc,"is hidden",hidenin)

def explore(name):
	playerc = bcolors.Player+name.strip()+bcolors.ENDC
	finds = ["explores a forest","explores a lake","found a fire but ran away","explores a forest","found a cave"]
	cindex = int(srandom.randrange(0, len(finds)))
	found = finds[cindex].strip()
	print(playerc,found)

def other(player, oplayer):
	if player.strip() in deadinround:
		return
	if oplayer.strip() in deadinround:
		oplayer = "somebody"
	if player.strip() not in aliveplayers:
		return
	if oplayer.strip() not in aliveplayers:
		oplayer = "somebody"
	playerc = bcolors.Player+player.strip()+bcolors.ENDC
	oplayerc = bcolors.oPlayer+oplayer.strip()+bcolors.ENDC
	randomother = random.choice(["a","b","c","d","e","f","g","h"])
	if randomother == "a":
		print(playerc,"and ",oplayerc," run into each other and decide to truce for the night.")
	elif randomother == "b":
		print(playerc,"destroys ",oplayerc,"'s supplies while is asleep.")
	elif randomother == "c":
		print(playerc,"sings him/herself to sleep")
	elif randomother == "d":
		print(playerc,"and ",oplayerc," huddle for warmth")
	elif randomother == "e":
		print(playerc,"overhears ",oplayerc," talking in the distance and runs away.")
	elif randomother == "f":
		print(playerc,"convince",oplayerc,"to snuggle with him/her")
	elif randomother == "g":
		print(playerc,"passes out from exhaustion")
	elif randomother == "h":
		print(playerc,"picks flowers")

def receive(name):
	playerc = bcolors.Player+name.strip()+bcolors.ENDC
	objects = ["a bow","clean water","fresh food","explosives","some medical supplies","a sword","arrows","a bow and arrows","a hatchet"]
	bindex = int(srandom.randrange(0, len(objects)))
	got = objects[bindex].strip()
	print(playerc,"has found",got,"from unknown sponsor")

def killaction(name,oplayer):
	playerc = bcolors.Player+name.strip()+bcolors.ENDC
	oplayerc = bcolors.oPlayer+oplayer.strip()+bcolors.ENDC
	deaths = ["knife","spear","sword","animal","stabbed","ambush","explosion"]
	animals = ["a boar","a wild centor","a snake bite","a scorpion","a hare (what a shame)","an unknown monster","a jaguar", "a panthere", "a poisonous frog", "a caiman"]

	yindex = int(srandom.randrange(0, len(deaths)))
	playerdeath = deaths[yindex].strip()

	mindex = int(srandom.randrange(0, len(animals)))
	animal = animals[mindex].strip()

	if playerdeath == "knife":
		print(playerc,"thrown a knife at",oplayerc,"!") 
		kill(oplayer)
	elif playerdeath == "spear":
		print(playerc,"died after being pierced with a spear by",oplayerc,".")
		kill(name)
	elif playerdeath == "sword":
		print(playerc,"killed",oplayerc,"with a sword.")
		kill(oplayer)
	elif playerdeath == "animal":
		print(playerc,"was killed by",animal,".")
		kill(name)
	elif playerdeath == "stabbed":
		print(playerc,"was stabbed with a dagger by",oplayerc,"!")
		kill(name)
	elif playerdeath == "ambush":
		print(playerc,"was ambushed and killed by",oplayerc)
		kill(name)
	elif playerdeath == "explosion":
		print(oplayerc,"set up explosives and killed",playerc)
		kill(player)
	else:
		print(player,"died from unknown reasons.")
		kill(name)

#LIST OF RANDOM ACTION
def randomact(player, day):
	playing = True
	randomIndex2 = int(srandom.randrange(0, len(aliveplayers)))
	oplayer = aliveplayers[randomIndex2].strip()
	while (player == oplayer) and (oplayer in deadinround):
		randomIndex2 = int(srandom.randrange(0, len(aliveplayers)))
		oplayer = aliveplayers[randomIndex2].strip()
	if len(aliveplayers)==1:
		return
	if day == 1 and (player in aliveplayers):
		actions = "runaway,runaway,runaway,runaway,runaway,runaway,hide,explore,gather,hide,explore,gather,die,spare,find,lost,sanity,spare,runaway,find,find,find,runaway,lost,random,runwaway,follow,runaway"
	elif day < 3 and day > 1 and (player in aliveplayers):
		actions = "die,sleep,sleep,sleep,sleep,sleep,kill,spare,sleep,find,lost,sanity,spare,kill,find,find,kill,find,sanity,lost,random,spare,follow,group"	
	elif day < 5 and day > 3:
		actions = "kill,kill,tend,sad,sleep,sleep,sleep,sleep,tend,tend,tend,tend,spare,find,lost,sanity,tend,spare,kill,scream,scream,tend,kill,find,die,sanity,lost,random,spare,follow,group,suicide"
	elif (player not in deadinround):
		actions = "die,kill,tend,sad,tend,tend,kill,kill,kill,kill,other,other,scream,kill,spare,find,lost,scream,scream,scream,sanity,sanity,kill,scream,scream,tend,kill,find,sanity,lost,random,spare,follow,group,suicide"
	else:
		playing == False
		actions = "not,playing"

	actions = actions.split(',')
	randomIndex = int(srandom.randrange(0, len(actions)))
	randomAction = actions[randomIndex]
	playerc = bcolors.Player+player.strip()+bcolors.ENDC
	oplayerc = bcolors.oPlayer+oplayer.strip()+bcolors.ENDC
	if randomAction == "find":
		receive(player)
	elif randomAction == "spare":
		if player.strip() == oplayer.strip():
			oplayer = "somebody"
		print(playerc, "fought with ",oplayerc," but spared his victim")
	elif randomAction == "lost":
		print(playerc,"is lost in the forest")
	elif randomAction == "kill":
		killaction(player,oplayer)
	elif randomAction == "die":
		print(playerc,"fell into a pit!")
		kill(player)
	elif randomAction == "sanity":
		print(playerc,"questions his/her sanity")
	elif randomAction == "group":
		print(playerc,"is now in a group with ",oplayerc,"!")
	elif randomAction == "follow":
		print(playerc, "now follows ",oplayerc,"!")
	elif randomAction == "runaway":
		print(playerc,"runs away from the Cornucopia")
	elif randomAction == "scream":
		print(playerc,"screams for help")
	elif randomAction == "sad":
		print(playerc,"thinks about home")
	elif randomAction == "hunt":
		hunt(player, oplayer)
	elif randomAction == "gather":
		print(playerc,"is gathering food!")
	elif randomAction == "hide":
		hide(player, oplayer)
	elif randomAction == "explore":
		explore(player)
	elif randomAction == "sleep":
		print(playerc,"tries to sleep!")
	elif (playing):
		other(player,oplayer)

#FUNCTION TO KILL PLAYER
def kill(player):
	playerc = bcolors.Player+player.strip()+bcolors.ENDC
	if player in aliveplayers:
		aliveplayers.remove(player.strip())
		deadinround.append(player.strip())
		print(playerc,"is now DEAD!")

#GONGS AT THE END OF THE GAME
def gongs(day):
	if len(deadinround)>0:
		time.sleep(2)
		if len(deadinround)==1:
			print("\n \n \n")
			print(bcolors.RED,"The players now hears",len(deadinround),"gong",bcolors.ENDC)
		else:
			print("\n \n \n")
			print(bcolors.RED,"The players now hears",len(deadinround),"gongs",bcolors.ENDC)
		time.sleep(2)
		for x in range(len(deadinround)): 
			print("\n \n",bcolors.Player,deadinround[x],bcolors.ENDC,bcolors.RED,"died today!",bcolors.ENDC," \n \n")
#GAME FINISHED
def finish():
	time.sleep(2)
	print("Game is finished")
	for x in range(len(aliveplayers)): 
			print("\n",bcolors.Player,aliveplayers[x],bcolors.ENDC,"has",bcolors.Player,"won!",bcolors.ENDC)

#GAME LOOP
i = 1
while len(aliveplayers) > 1:
	deadinround = []
	print("\n \n \n",bcolors.DAY,"Day",i,bcolors.ENDCO,"\n \n \n")
	unplayed = aliveplayers.copy()
	while len(unplayed) > 0:
		randomPlayer = int(srandom.randrange(0, len(unplayed)))
		chosedplayer = unplayed[randomPlayer]
		randomact(chosedplayer, i)
		unplayed.remove(chosedplayer)
		time.sleep(1.5)
	unplayed = aliveplayers.copy()
	i += 1
	gongs(i)
	continueame = input("Press enter to continue!")
if len(aliveplayers) == 1:
	finish()












