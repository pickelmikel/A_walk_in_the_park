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




prompt_help = """

To see more detailed help, type 'instructions' #TODO

Press 'i' or type 'inventory' to current list of items
in your hands, in your pockets, and in your backpack.

Press 'q' or type 'quit' to end the game.

"""









#### ---- PLACE DESCRIPTIONS ---- ####



# PATH (STARTING POINT)
land_0 = ("""\nYou are at a trail intersection.  There is a kiosk with a map. 
You can go east, west, or south.\n""")


# ALONG THE RIVER
land_1 = ("""\nThe musty smell of the air and roar of a river invite you to sit for awhile.
You can go east or north\n""")


# MOUNTAINOUS OVERLOOK
land_2 = ("""\nWhat a view, wish you could see.
You can only go west\n""")


# DARK FOREST
land_3 = ("""\nYou have found yourself in a dark forest...it's kind of spooky
You can go north, east, or south.\n""")


# MUSHROOM HOUSE
land_4 = ("""\nYou see a house made from a mushroom.  There is a garden to the north.
You can go north or west""")

land_4_house_0 = ("""\nIt smells like mushrooms in this house.
There is a room to the west and a room to the east.  
The door to the outside is south.
\n""")

land_4_house_outside = ("""\nIt's a mushroom...that's a HOUSE!\n""")

land_4_house_1 = ("""\nThis looks like a bed room with a large soft bed and a closet.
\n""")

land_4_house_2 = ("""\nA small table stands in the center of this room.
There is a doorway to the north and east
\n""")

land_4_house_3 = ("""\nThere are cupboards lining the walls and a small counter with dishes.
A wood buring stove sits in the east corner.\n""")

# FAIRY GARDEN
land_5 = ("""\nThe garden is full of fairies dancing among the veggies.
A path skirting the dense forest leads to the west and a mushroom house to the south.\n""")


# EDGE OF DARK FOREST
land_6 = ("""\nYou are along a rocky ledge that looks down into a steep canyon to the north.
There is a path to the south that disappers into a dense forest.
There is a path to the east and west.\n""")


# NOT SURE YET
land_7 = ("""\nNothing here yet...
You can go east or south.\n""")


# LAKE
land_8 = ("""\nThere's a large lake to the south and a path to the west.\n
""")


# WILD FLOWER PRARIE
land_9 = ("""\nYou have entered a large field of wild flowers.
The path leads to the north and east.\n""")


# PINE FOREST
land_10 =("""\nYou have entered an amazing pine forest.  The smell of the forest is overwhelming.
The path leads east and south.\n""")


# PARKING LOT (START/ENDING)

land_11_start = ("""
As you drive into the trailhead parking lot, the old sign
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

land_11 = ("""
You are in the trail head parking area. There are five vehicles
parked here, including yours.  The trail goes north between some trees and there is 
a sign on the left side of the trail""")

land_11_tree = ("""

It's a beautiful   ##
pine tree         ####
                 ######
                ######## 
                   ||
                   ||


""")

land_11_sign = ("""
The sign reads:

Welcome to Trailhead Wilderness Area
Please keep it tidy...""")





land_11_ending = ("""\nYou made it back to the parking lot where your vehicle has been waiting for your safe return.

Would you like to go back to the forest, or drive home?
"Type north to return or quit to go home?"\n""")


# SECRET CAVE
#land_12_desc =




land_map = '''

--------------------------------------------------------------
|                                                            |
|                                                            |
|                                                            |
|                                                            |
|                                                            |
|                                                            |
|                                                            |
|                                                            |
|                                                            |
|                                                            |
|                                                            |
|                                                            |
|                                                            |
|                                                            |
|                                                            |
|                                                            |
|                                                            |
|                                                            |
|                                                            |
|                          =========||==========             |
|                                   ||                       |
|                                 __||__                     |
|             You are ------->   |      |                    |
|              here              |      |                    |
|                                |      |                    |
--------------------------------------------------------------
'''
