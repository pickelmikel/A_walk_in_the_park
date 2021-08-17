

#### ---- PLAYER STUFF ---- ####
player_name_list = []
player_inv_hand = [False, False]
player_inv_pocket = [False, False,]
player_inv_backpack = [False, False, False]
saved_file_list = ["Fuger","Gakwith","Nerthal"]
prev_grid = [0]
curr_grid = [0]
visited_0 = [0]
visited_1 = []
visited_2 = []
visited_3 = []
visited_4 = []
visited_5 = []
visited_6 = []
visited_7 = []
visited_8 = []
visited_9 = []
visited_10 = []
visited_11 = {}
visited_12 = []
visited_list = []
#### ---- PLAYER INFO DICTONARY ---- ####



#player_slot_0 = defaultdict(
 #   'player_name', player_name,
  #  'last_location',prev_grid,
   # 'current_location',curr_grid,
    #'player_inv_hand_left',player_inv_hand,
    #'player_inv_hand_right',player_inv_hand,
    #'player_inv_backpack_0',player_inv_backpack,
    #'player_inv_backpack_1',player_inv_backpack,
    #'player_inv_backpack_2',player_inv_backpack,
    #'player_inv_pocket_0',player_inv_pocket,
    #'player_inv_pocket_1',player_inv_pocket)








#### ---- VARIABLES ---- ####

leave_game = ("quit", "q")
west = ("west", "w")
east = ("east", "e")
north = ("north", "n")
south = ("south", "s")
yes = ("yes", "y", "ok", "okay", "k", "sure", "yeah", "ya", "totally", "you bet")
no = ("no", "n", "na", "nope", "nay")

what_to_do = "\nWhat would you like to do?: "


#### ---- INSTRUCTIONS ---- ####

instructions = ("""\nThese are the instructions to play the game...

If you want to go a direction, type the direction or first letter 
of the direction you with to travel

Like: 'north' or 'n'

To enter a structure type something

Like: 'enter house'

To look closer at an object type 'look' then the name of the object

Like: 'look person' or 'look tree'

Also if you want to talk to people you meet say 'talk' 

Like: 'talk person' or 'talk tree'

You may also type 'quit' or 'q' to leave the game

...more to come.""")


#### ---- PLACE DESCRIPTIONS ---- ####



# PATH (STARTING POINT)
land_0_desc = ("""\nYou found yourself here, now what? 
You can go east or west\n""")


# ALONG THE RIVER
land_1_desc = ("""\nThe musty smell of the air and roar of a river invite you to sit for awhile.
You can go east or north\n""")


# MOUNTAINOUS OVERLOOK
land_2_desc = ("""\nWhat a view, wish you could see.
You can only go west\n""")


# DARK FOREST
land_3_desc = ("""\nYou have found yourself in a dark forest...it's kind of spooky
You can go north, east, or south.\n""")


# MUSHROOM HOUSE
land_4_desc = ("""\nYou see a house made from a mushroom.  There is a garden to the north.
You can go north or west""")

land_4_desc_house_0 = ("""\nIt smells like mushrooms in this house.
There is a room to the west and a room to the east

What would you like to do?\n""")

land_4_desc_house_outside = ("""\nIt's a mushroom...that's a HOUSE!\n""")

land_4_desc_house_1 = ("""\nThis looks like a bed room with a large soft bed and a closet.

What would you like to do?\n""")

land_4_desc_house_2 = ("""\nA small table stands in the center of this room.
There is a doorway to the north and east

What would you like to do?\n""")

land_4_desc_house_3 = ("""\nThere are cupboards lining the walls and a small counter with dishes.
A wood buring stove sits in the east corner.\n""")

# FAIRY GARDEN
land_5_desc = ("""\nThe garden is full of fairies dancing among the veggies.
A path skirting the dense forest leads to the west and a mushroom house to the south.\n""")


# EDGE OF DARK FOREST
land_6_desc = ("""\nYou are along a rocky ledge that looks down into a steep canyon to the north.
There is a path to the south that disappers into a dense forest.
There is a path to the east and west.\n""")


# NOT SURE YET
land_7_desc = ("""\nNothing here yet...
You can go east or south.\n""")


# LAKE
land_8_desc = ("""\nThere's a large lake to the south and a path to the west.\n
""")


# WILD FLOWER PRARIE
land_9_desc = ("""\nYou have entered a large field of wild flowers.
The path leads to the north and east.\n""")


# PINE FOREST
land_10_desc =("""\nYou have entered an amazing pine forest.  The smell of the forest is overwhelming.
The path leads east and south.\n""")


# PARKING LOT (START/ENDING)

land_11_desc_0_start = ("""As you drive into the trailhead parking lot, the old sign
 saying "Welcome to Trailhead Springs Wilderness Area" greets you on the right.
 There are four other vehicles in the small parking area. You park next to one of
 the vehicles, a bright red Jeep. As you open the door from your long drive
 the smell of pine enters your nose and a pleasent tingle travels down your spine.
 
 While standing at your vehicle with the afternoon sun warming your skin and the 
 cool mountain air cooling the warmth it feeles just a little chilly.  Feeling 
 grateful you have your warm coat and backpack with your lightweight, yet warm
 sleeping bag, and lightweight one person tent.
 
 You are ready to go...There is a dirt trail that leads towards the north through 
 some trees.  There is a sign just past the edge of the parking lot on the left
 side of the trail. """)

land_11_desc_0 = ("""You are in the trail head parking area. There are five vehicles
parked here, including yours.  The trail goes north between some trees and there is 
a sign on the left side of the trail.""")

land_11_desc_tree = ("""It's a tree""")

land_11_desc_sign = ("""The sign reads:

Welcome to Trailhead Wilderness Area
Please keep it tidy...""")





land_11_desc_ending = ("""\nYou made it back to the parking lot where your vehicle has been waiting for your safe return.

Would you like to go back to the forest, or drive home?
"Type north to return or quit to go home?"\n""")


# SECRET CAVE
#land_12_desc =



#### --- GENERAL DEFINITIONS --- ####
def leave_game_now():
    print("\n\nSee ya later,", player_name_list[0])
    quit()
    

def greet():
    print("Greetings!\n\nWelcome to this adventure...")
    answer=input("\n\nWould you like instructions?\n")
    for i in yes:
        if answer.lower() in yes:
            print(instructions)
            break
    else:
        print("Ahh, you already know how to play")



def new_player():
	player_name=input("Lets get you setup with our outfitter.\n\nWhat is the full name \
of your adventurer?\n")
	player_name_list.append(player_name)

def newvisit11():
	if newv in visited_11:
		visited_11.append(newv + 1)



#### --- LAND DEFINITIONS --- ####

def land_0(): # STARTING POINT...for now
    curr_grid = 0
    print(land_0_desc)
    answer=input(what_to_do)
    for i in west:
        if answer.lower() in west:
            prev_grid = 0
            land_1()
    for j in east:
        if answer.lower() in east:
            prev_grid = 0
            land_2()
    for m in leave_game:
        if answer.lower() in leave_game:
            leave_game_now()
    else:
        land_0()


def land_1(): # ALONG THE RIVER
    curr_grid = 1
    print(land_1_desc)
    answer=input(what_to_do)
    for i in east:
        if answer.lower() in east:
            prev_grid = 1
            land_0()
    for j in north:
        if answer.lower() in north:
            prev_grid = 1
            land_3()
    for m in leave_game:
        if answer.lower() in leave_game:
            leave_game_now()
    else:
        land_1()
        
        
def land_2(): # MOUNTAINOUS OVERLOOK
    curr_grid = 2
    print(land_2_desc)
    answer=input(what_to_do)
    for i in west:
        if answer.lower() in west:
            prev_grid = 2
            land_0()
    for m in leave_game:
        if answer.lower() in leave_game:
            leave_game_now()
    else:
        land_2()


def land_3(): # DARK FOREST
    curr_grid = 3
    print(land_3_desc)
    answer=input(what_to_do)
    for i in north:
        if answer.lower() in north:
            prev_grid = 3
            land_6()
    for j in east:
        if answer.lower() in east:
            prev_grid = 3
            land_4()
    for k in south:
        if answer.lower() in south:
            prev_grid = 3
            land_1()
    for m in leave_game:
        if answer.lower() in leave_game:
            leave_game_now()
    else:
        land_3()


def land_4(): # MUSHROOM HOUSE
    curr_grid = 4
    print(land_4_desc)
    answer=input(what_to_do)
    for i in north:
        if answer.lower() in north:
            prev_grid = 4
            land_5()
    for j in west:
        if answer.lower() in west:
            prev_grid = 4
            land_3()
    for m in leave_game:
        if answer.lower() in leave_game:
            leave_game_now()
    if answer.lower() == "enter house":
        land_4_house_0()
    if answer.lower() == "look house":
        print(land_4_desc_house_outside)
    for m in leave_game:
        if answer.lower() in leave_game:
            leave_game_now()
    else:
        land_4()
        

def land_4_house_0(): 
    curr_grid = 40
    print(land_4_desc_house_0)
    answer=input(what_to_do)
    for a in west:
        if answer.lower() in west:
            prev_grid = 40
            land_4_house_1()
    for b in east:
        if answer.lower() in east:
            prev_grid = 40
            land_4_house_2()
    for c in south:
        if answer.lower() in south:
            prev_grid = 40
            land_4()
    for m in leave_game:
        if answer.lower() in leave_game:
            leave_game_now()
    else:
        land_4_house_0()

def land_4_house_1():
    curr_grid = 41
    print(land_4_desc_house_1)
    answer=input(what_to_do)
    for a in east:
        if answer.lower() in east:
            prev_grid = 41
            land_4_house_0()
    for m in leave_game:
        if answer.lower() in leave_game:
            leave_game_now()
    else:
        land_4_house_1()

def land_4_house_2():
    curr_grid = 42
    print(land_4_desc_house_2)
    answer=input(what_to_do)
    for a in north:
        if answer.lower() in north:
            prev_grid = 42
            land_4_house_3()
    for b in east:
        if answer.lower() in east:
            prev_grid = 42
            land_4_house_0()
    for m in leave_game:
        if answer.lower() in leave_game:
            leave_game_now()
    else:
        land_4_house_2()

def land_4_house_3():
    curr_grib = 43
    print(land_4_desc_house_3)
    answer=input(what_to_do)
    for a in south:
        if answer.lower() in south:
            prev_grid = 42
            land_4_house_2()
    for m in leave_game:
        if answer.lower() in leave_game:
            leave_game_now()
    else:
        land_4_house_3()


def land_5(): # FAIRY GARDEN
    curr_grid = 5
    print(land_5_desc)
    answer=input(what_to_do)
    for i in west:
        if answer.lower() in west:
            prev_grid = 5
            land_6()
    for j in south:
        if answer.lower() in south:
            prev_grid = 5
            land_4()
    if answer.lower() == "talk fairy":
        talk_fairy_0()    
    for m in leave_game:
        if answer.lower() in leave_game:
            leave_game_now()
    else:
        land_5()
        

def land_6(): # EDGE OF DARK FOREST
    curr_grid = 6
    print(land_6_desc)
    answer=input(what_to_do)
    for i in west:
        if answer.lower() in west:
            prev_grid = 6
            land_7()
    for j in east:
        if answer.lower() in east:
            prev_grid = 6
            land_5()
    for k in south:
        if answer.lower() in south:
            prev_grid = 6
            land_3()
    for m in leave_game:
        if answer.lower() in leave_game:
            leave_game_now()
    else:
        land_6()


def land_7(): # NOT SURE YET
    curr_grid = 7
    print(land_7_desc)
    answer=input(what_to_do)
    for i in west:
        if answer.lower() in west:
            prev_grid = 7
            land_10()
    for j in east:
        if answer.lower() in east:
            prev_grid = 7
            land_6()
    for k in south:
        if answer.lower() in south:
            prev_grid = 7
            land_8()
    for m in leave_game:
        if answer.lower() in leave_game:
            leave_game_now()
    else:
        land_7()


def land_8(): # LAKE
    curr_grid = 8
    print(land_8_desc)
    answer=input(what_to_do)
    for i in north:
        if answer.lower() in north:
            prev_grid = 8
            land_7()
    for j in west:
        if answer.lower() in west:
            prev_grid = 8
            land_9()
    for m in leave_game:
        if answer.lower() in leave_game:
            leave_game_now()
    else:
        land_8()
        
        
def land_9(): # WILD FLOWER PRARIE
    curr_grid = 9
    print(land_9_desc)
    answer=input(what_to_do)
    for i in north:
        if answer.lower() in north:
            priv_grid = 9
            land_10()
    for j in east:
        if answer.lower() in east:
            prev_grid = 9
            land_8()
    for m in leave_game:
        if answer.lower() in leave_game:
            leave_game_now()
    else:
        land_9()
        

def land_10(): # PINE FOREST
    curr_grid = 10
    print(land_10_desc)
    answer=input(what_to_do)
    for i in east:
        if answer.lower() in east:
            prev_grid = 10
            land_7()
    for j in south:
        if answer.lower() in south:
            prev_grid = 10
            land_8()
    for m in leave_game:
        if answer.lower() in leave_game:
            leave_game_now()
    else:
        land_10()


def land_11(): # PARKING LOT (BEGIN/ENDING)
	curr_grid = 11
	#if newvisit11(newv) <= 0:
	#	print(land_11_desc_0_start)
	#if newvisit11(newv) <= 5:
	#	print(land_11_desc_0)
	answer=input(what_to_do)
	for a in north:
		if answer.lower() in north:
			prev_grid = 11
			newvisit11()
			#visited_11.append)
			land_0()
	if answer.startswith("look") and answer.endswith("tree"):
		print(land_11_desc_tree)
	if answer.lower() == "look at sign":
		print(land_11_desc_sign)
		land_11()
	for b in leave_game:
		if answer.lower() in leave_game:
			leave_game_now()
			
	else:
		land_11()


#def land_12 # SECRET CAVE
        
def talk_fairy_0():
    print("""\nYou open your mouth to speak, yet no words come out.
    They seem to be busy at the moment\n""")
    land_5()
    
#### ---- END ---- ####




#### ---- PROGRAM RUN CODE ---- ####



greet()
new_player()
print("Hey,", player_name_list[0], "\n")





land_11()






#### ---- END RUN CODE ---- ####










#### ---- EOF ---- ####
