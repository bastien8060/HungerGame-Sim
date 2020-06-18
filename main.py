#!/bin/python

#SETUP
import random
import time
import sys
global crazyness
import math

characterlist = ""
deadinround = [] 
wounded = []
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
	characterlist = ",Percy Jackson,Annabeth Chase,Jason Grace,Piper McLean,Frank Zhang,Hazel Levesque,Leo Valdez,Calypso,Grover Underwood,Tyson,Thalia Grace,Luke Castellan,Nico Di Angelo,Bianca Di Angelo,Clarisse La Rue,Silena Beauregard,Mr. D,Chiron,Rachel E. Dare,Zoe Nightshade,Reyna R.A,Hylla R.A,Octavian,Bastien"
else:
	amountPeople = int(input("How much characters?  "))
	while i<amountPeople:
		i += 1
		character = input("Name of character n"+str(i)+":  ")
		characterlist += ","+str(character)

crazyness = (-amountPeople / 4)*3



#MAKE A LIST FROM LIST OF CHARACTERS
characterlist = characterlist[1:]
characterlist = characterlist.split(',')
aliveplayers = characterlist.copy()


#FUNCTION WHEN PLAYER HUNTS SOMETHING
def hunt(name,oplayer):
	playerc = bcolors.Player+name.strip()+bcolors.ENDC
	oplayerc = bcolors.oPlayer+oplayer.strip()+bcolors.ENDC
	hunted = ["food","rabbit",oplayerc,"doe","fish"]
	oindex = int(srandom.randrange(0, len(hunted)))
	hunteditem = hunted[oindex].strip()
	print(playerc,"hunted",hunteditem)


#FUNCTION WHEN PLAYER HIDES SOMEWHERE
def hide(name, oplayer):
	playerc = bcolors.Player+name.strip()+bcolors.ENDC
	oplayerc = bcolors.oPlayer+oplayer.strip()+bcolors.ENDC
	hides = ["in the forest","in a tree","from "+oplayerc+" in a bush","in a bush","in a tree"]
	uindex = int(srandom.randrange(0, len(hides)))
	hidenin = hides[uindex].strip()
	print(playerc,"is hidden",hidenin)

#FUNCTION WHEN PLAYER EXPLORE SOMEHTHING/SOMEWHERE
def explore(name):
	playerc = bcolors.Player+name.strip()+bcolors.ENDC
	finds = ["explores a forest","explores a lake","found a fire but ran away","explores a forest","found a cave"]
	cindex = int(srandom.randrange(0, len(finds)))
	found = finds[cindex].strip()
	print(playerc,found)
	crazy(name)

#FUNCTION FOR OTHER USELESS ACTIONS THAT THE PLAYER COULD MAKE
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
	randomother = random.choice(["a","b","c","d","e","f","g","h","i","j","k"])
	if randomother == "a":
		print(playerc,"and ",oplayerc," run into each other and decide to truce for the night.")
		uncrazy(player)
	elif randomother == "b":
		print(playerc,"destroys ",oplayerc,"'s supplies while is asleep.")
		crazy(player)
	elif randomother == "c":
		print(playerc,"sings him/herself to sleep")
		crazy(player)
	elif randomother == "d":
		print(playerc,"and ",oplayerc," huddle for warmth")
		uncrazy(player)
	elif randomother == "e":
		print(playerc,"overhears ",oplayerc," talking in the distance and runs away.")
		crazy(player)
	elif randomother == "f":
		print(playerc,"convince",oplayerc,"to snuggle with him/her")
		uncrazy(player)
	elif randomother == "g":
		print(playerc,"passes out from exhaustion")
		crazy(player)
	elif randomother == "h":
		print(playerc,"picks flowers")
		crazy(player)
	elif randomother == "i":
		tend(player)
	elif randomother == "j":
		tend(player)
	elif randomother == "k":
		tend(player)


#FUNCTION WHEN PLAYER RECEIVES AN OBJECT FROM AN UNKNOWN SPONSOR
def receive(name):
	playerc = bcolors.Player+name.strip()+bcolors.ENDC
	objects = ["a bow","clean water","fresh food","explosives","some medical supplies","a sword","arrows","a bow and arrows","a hatchet"]
	bindex = int(srandom.randrange(0, len(objects)))
	got = objects[bindex].strip()
	print(playerc,"has found",got,"from unknown sponsor")

#DIFFERENT ACCIDENTAL DEATHS SCENARIOS:
def aciddentaldeaths(name):
	playerc = bcolors.Player+name.strip()+bcolors.ENDC
	accidentaldeaths = ["starved","thirst","climb","drown","sunstroke","cold","mine","pit"]

	findex = int(srandom.randrange(0, len(accidentaldeaths)))
	playerdeath = accidentaldeaths[findex].strip()

	if playerdeath == "starved":
		print(playerc,"died of hunger!") 
		kill(name)
	elif playerdeath == "thirst":
		print(playerc,"died of thirst.")
		kill(name)
	elif playerdeath == "climb":
		print(playerc,"Fell while climbing a tree and died.")
		kill(
			player)
	elif playerdeath == "drown":
		print(playerc,"drown himself in the river.")
		kill(name)
	elif playerdeath == "sunstroke":
		print(playerc,"died of a sunstroke!")
		kill(name)
	elif playerdeath == "cold":
		print(playerc,"froze to death")
		kill(name)
	elif playerdeath == "mine":
		print(oplayerc,"accidentally found a lost mine. He/She exploded")
		kill(name)
	elif playerdeath == "pit":
		print(playerc,"fell into a pit")
		kill(name)
	else:
		print(name,"died from unknown reasons.")
		kill(name)



#FUNCTION FOR DIFFERENTS KILL/DIE SCENARIOS
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
		kill(name)
	else:
		print(name,"died from unknown reasons.")
		kill(name)

#MAIN LIST OF RANDOM ACTION
def randomact(player, day):
	global crazyness
	playing = True
	randomIndex2 = int(srandom.randrange(0, len(aliveplayers)))
	oplayer = aliveplayers[randomIndex2].strip()
	while (player == oplayer) and (oplayer in deadinround):
		randomIndex2 = int(srandom.randrange(0, len(aliveplayers)))
		oplayer = aliveplayers[randomIndex2].strip()
	if len(aliveplayers)==1:
		return
	if crazyness > 8:
		actions = "othercrazy,tendself,tendself,kill,die,kill,tendself,othercrazy,tendself,wound,tendself,kill,othercrazy,othercrazy,kill,tendself,suicide,lost,tend,find,othercrazy,wound,random,follow,sanity,group"
	elif day == 1 and (player in aliveplayers):
		actions = "wound,runaway,tendself,runaway,wound,kill,runaway,tendself,runaway,kill,runaway,find,tendself,wound,tend,hide,explore,kill,tendself,gather,wound,lost,sanity,spare,kill,runaway,find,runaway,lost,random,runwaway,die,follow,runaway"
	elif day < 3 and day > 1 and (player in aliveplayers):
		actions = "die,sleep,other,sleep,sleep,tendself,sleep,kill,other,sleep,find,other,other,wound,tend,tendself,other,wound,other,wound,kill,find,tendself,sanity,kill,wound,lost,random,spare,follow,group"	
	elif day < 5 and day > 3:
		actions = "kill,kill,tend,sad,sleep,tendself,sleep,sleep,kill,tend,lost,sanity,tendself,other,wound,tend,kill,scream,scream,other,other,wound,tendself,find,die,lost,kill,random,spare,other,other,follow,group,suicide"
	elif (player not in deadinround):
		actions = "die,kill,tend,other,sad,tendself,kill,wound,wound,kill,kill,kill,other,tendself,other,tend,wound,scream,kill,find,lost,kill,scream,scream,scream,kill,sanity,sanity,kill,other,other,other,other,scream,scream,tend,kill,other,sanity,lost,random,kill,follow,group,suicide,spare"
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
		crazyauto()
	elif randomAction == "lost":
		print(playerc,"is lost in the forest")
		crazy(player)
	elif randomAction == "kill":
		killaction(player,oplayer)
	elif randomAction == "die":
		aciddentaldeaths(player)
		kill(player)
	elif randomAction == "sanity":
		print(playerc,"questions his/her sanity")
		crazy(player)
	elif randomAction == "group":
		print(playerc,"is now in a group with ",oplayerc,"!")
		uncrazy(player)
	elif randomAction == "follow":
		print(playerc, "now follows ",oplayerc,"!")
		uncrazy(player)
	elif randomAction == "runaway":
		print(playerc,"runs away from the Cornucopia")
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
		crazyauto()
	elif randomAction == "othercrazy":
		crazyactions(player)
	elif randomAction == "wound":
		wound(player,oplayer)
	elif randomAction == "tend":
		tend(player)
	elif (playing):
		other(player,oplayer)


#FUNCTION TO WHEN PLAYER GETS MORE CRAZY
def crazy(player):
	playerc = bcolors.Player+player.strip()+bcolors.ENDC
	global crazyness
	if player == "":
		crazyness += 2
		print("Everyone's mood turn a bit sad and crazy")
	else:
		crazyness += 1
		if crazyness == 2:
			print(playerc,"is slowly going crazy...")
		elif crazyness == 4:
			print(playerc,"is slowly going crazy...")
		elif crazyness == 6:
			print(playerc,"is slowly going crazy...")
		elif crazyness == 8:
			print(playerc,"is slowly going crazy...")
		elif crazyness > 8:
			print(playerc,"is slowly going crazy...")

#FUNCTION TO WHEN EVERYONE GETS MORE CRAZY
def crazyauto():
	global crazyness
	crazyness += 2

#FUNCTION TO WHEN PLAYER GETS LESS CRAZY
def uncrazy(player):
	playerc = bcolors.Player+player.strip()+bcolors.ENDC
	global crazyness
	crazyness -= 1
	print(playerc,"feels a bit better")

#FUNCTION CONTAINING ACTIONS THAT CRAZY PLAYERS WILL DO
def crazyactions(player):
	randomIndex2 = int(srandom.randrange(0, len(aliveplayers)))
	oplayer = aliveplayers[randomIndex2].strip()
	while (player == oplayer) and (oplayer in deadinround):
		randomIndex2 = int(srandom.randrange(0, len(aliveplayers)))
		oplayer = aliveplayers[randomIndex2].strip()
	if len(wounded)>0:
		crazyactions = "scream,sad,halucinate,other,tend,tend,tend,other,kill,suicide,wound"
	else:
		crazyactions = "scream,sad,halucinate,other,other,kill,suicide,wound"
	crazyactions = crazyactions.split(',')
	gIndex = int(srandom.randrange(0, len(crazyactions)))
	randomCraziness = crazyactions[gIndex]
	playerc = bcolors.Player+player.strip()+bcolors.ENDC
	oplayerc = bcolors.Player+oplayer.strip()+bcolors.ENDC
	if randomCraziness == "scream":
		print(playerc,"is losing his/her mind.",playerc,"screams in the wild!")
		crazy(player)
	elif randomCraziness == "sad":
		print(playerc,"thinks about home")
		crazy(player)
	elif randomCraziness == "halucinate":
		print(playerc,"is halucinating.",playerc," sees his/her parents")
		crazy(player)
	elif randomCraziness == "other":
		print(playerc,"is halucinating.",playerc," sees his/her parents")
		other(player, oplayer)
	elif randomCraziness == "kill":
		print(player,"kills",oplayerc,"for no reason")
		kill(oplayer)	
	elif randomCraziness == "suicide":
		print(playerc,"stabs him/herself")
		kill(player)
	elif randomCraziness == "wound":
		wound(player,oplayer)
	elif randomCraziness == "tend":
		tend(player)


#FUNCTION TO WOUND THE PLAYER
def wound(player,oplayer):
	weapons = ["a knife","a sword","fire","an arrow","his/her friends","an unknown weapon","a dagger", "a wolf trap", "a poisonous arrow", "a wood stick"]
	pindex = int(srandom.randrange(0, len(weapons)))
	weapon = weapons[pindex].strip()
	playerc = bcolors.Player+player.strip()+bcolors.ENDC
	oplayerc = bcolors.oPlayer+oplayer.strip()+bcolors.ENDC
	wounded.append(player.strip())
	print(oplayerc,"wounded",playerc,"with",weapon)



#FUNCTION THAT KILLS THE WOUNDED PEOPLE THAT WERENT TENDED BY THE END OF THE GAME
def wounDie():
	for player in wounded:
		playerc = bcolors.oPlayer+player.strip()+bcolors.ENDC
		print(playerc,"died because of his wounds")
		print("\n")
		if player in aliveplayers:
			aliveplayers.remove(player)
		if player not in deadinround:
			deadinround.append(player)


#IF A PLAYER TENDS SOMEONE ELSE'S WOUNDS TO SAVE THEM
def tend(player):
	if len(wounded)==0:
		randomIndex2 = int(srandom.randrange(0, len(aliveplayers)))
		oplayer = aliveplayers[randomIndex2].strip()
		while (player == oplayer) and (oplayer in deadinround):
			randomIndex2 = int(srandom.randrange(0, len(aliveplayers)))
			oplayer = aliveplayers[randomIndex2].strip()
		other(player,oplayer)
	else:
		oplayer = wounded[0].strip()
		playerc = bcolors.Player+player.strip()+bcolors.ENDC
		oplayerc = bcolors.oPlayer+oplayer.strip()+bcolors.ENDC
		wounded.remove(oplayer)
		print(playerc,"tends",oplayerc+", healing his/her wounds")
		uncrazy(oplayer)
		uncrazy(player)

#IF PLAYER TENDS WOUNDS BY THEMSELVES
def tendself(player):
	if player not in wounded:
		randomIndex2 = int(srandom.randrange(0, len(aliveplayers)))
		oplayer = aliveplayers[randomIndex2].strip()
		while (player == oplayer) and (oplayer in deadinround):
			randomIndex2 = int(srandom.randrange(0, len(aliveplayers)))
			oplayer = aliveplayers[randomIndex2].strip()
		other(player,oplayer)
	else:
		playerc = bcolors.Player+player.strip()+bcolors.ENDC
		wounded.remove(player)
		print(playerc,"tends his own wounds, saving his/her life!")
		uncrazy(player)

#FUNCTION TO KILL PLAYER
def kill(player):
	playerc = bcolors.Player+player.strip()+bcolors.ENDC
	if player in aliveplayers:
		aliveplayers.remove(player.strip())
		deadinround.append(player.strip())
		print(playerc,"is now DEAD!")
		crazy("")

#GONGS AT THE END OF THE GAME
def gongs(day):
	if len(deadinround)>0:
		time.sleep(2)
		if len(deadinround)==1:
			print("\n \n \n")
			print(bcolors.RED,"The players now hears",len(deadinround),"canon shot",bcolors.ENDC)
		else:
			print("\n \n \n")
			print(bcolors.RED,"The players now hears",len(deadinround),"canon shots",bcolors.ENDC)
		time.sleep(2)
		for x in range(len(deadinround)): 
			print("\n \n",bcolors.Player,deadinround[x],bcolors.ENDC,bcolors.RED,"died today!",bcolors.ENDC," \n \n")
#GAME FINISHED
def finish():
	time.sleep(2)
	print("Game is finished")
	for x in range(len(aliveplayers)): 
			print("\n",bcolors.Player,aliveplayers[x],bcolors.ENDC,"has",bcolors.Player,"won!",bcolors.ENDC)

#TIME CONVERSION
def timeconvert(m):
	hours = 0
	min = 0
	while int(m) >= 60:
		m -= 60
		hours += 1
	min = m
	if hours <= 12:
		timeformat = "am"
	else:
		hours -= 12
		timeformat = "pm"


	if min != 0.0:
		min = int(min)
	
	
	if min == 0 or min == "0":
		min = "00"
	if int(min) < 10 and int(min) > 0:
		min = "0"+str(min)
	return str(hours)+":"+str(min)+timeformat



#GET TIME OF THE DAY:
def timeday(unplayed,total):
	i = total - unplayed
	i += 1
	each = 1440 / total
	return timeconvert(each * i) 

#GAME LOOP
i = 1
while len(aliveplayers) > 1:
	deadinround = []
	wounded = []
	print("\n \n \n",bcolors.DAY,"Day",i,bcolors.ENDCO,"\n \n \n")
	unplayed = aliveplayers.copy()
	while len(unplayed) > 0:

		print(timeday(len(unplayed),len(aliveplayers)))
		randomPlayer = int(srandom.randrange(0, len(unplayed)))
		chosedplayer = unplayed[randomPlayer]
		randomact(chosedplayer, i)
		unplayed.remove(chosedplayer)
		time.sleep(1.5)
		print("\n")
	unplayed = aliveplayers.copy()
	i += 1
	crazyauto()
	wounDie()
	gongs(i)
	continueame = input("Press enter to continue!")
if len(aliveplayers) == 1:
	finish()












