import land_desc


#### ---- PLAYER STUFF ---- ####
player_name = []


player_inv = [[False, False], [False, False], [False, False, False]]
hand_left, hand_right, pocket_left, pocket_right, backpack_1, backpack_2, backpack_3 = player_inv[0][0], player_inv[0][1], player_inv[1][0], player_inv[1][1], player_inv[2][0], player_inv[2][1], player_inv[2][2]

display_inv = (f'{hand_left} is in your left hand\n\
{hand_right} is in your right hand\n\
{pocket_left} is in your left pocket\n\
{pocket_right} is in your right pocket\n\
{backpack_1},{backpack_2}, and {backpack_3} are in your backpack')

saved_file_list = []
prev_land = []
curr_land = []
visited_0 = [0]
visited_1 = [0]
visited_2 = [0]
visited_3 = [0]
visited_4 = [0]
visited_5 = [0]
visited_6 = [0]
visited_7 = [0]
visited_8 = [0]
visited_9 = [0]
visited_10 = [0]
visited_11 = [0]
visited_12 = [0]
visited_list = []

db = "player name", player_name, "current land", curr_land, id(curr_land), "previous land", prev_land, id(prev_land)
    

#### ---- PLAYER INFO DICTIONARY ---- ####



#player_slot_0 = defaultdict(
 #   'player_name', player_name,
  #  'last_location',prev_land,
   # 'current_location',curr_land,
    #'player_inv_hand_left',player_inv_hand,
    #'player_inv_hand_right',player_inv_hand,
    #'player_inv_backpack_0',player_inv_backpack,
    #'player_inv_backpack_1',player_inv_backpack,
    #'player_inv_backpack_2',player_inv_backpack,
    #'player_inv_pocket_0',player_inv_pocket,
    #'player_inv_pocket_1',player_inv_pocket)







#4### ---- VARIABLES ---- ####

leave_game = ("quit", "q")
west = ("west", "w")
east = ("east", "e")
north = ("north", "n")
south = ("south", "s")
yes = ("yes", "y", "ok", "okay", "k", "sure", "yeah", "ya", "totally", "you bet", "yep")
no = ("no", "n", "na", "nope", "nay")
pl_inv = ("i", "inventory")


what_to_do = "\nWhat would you like to do?: "


#### --- GENERAL DEFINITIONS --- ####
def leave_game_now():
    answer=input("\n\nare you sure you want to quit? ").lower()
    if answer in yes:
        print("\n\nSee ya later,", player_name[0])
        quit()
    else:
        c_l()
    
def greet():
    print("Greetings!\n\nWelcome to this adventure...")
    answer=input("\n\nWould you like instructions?\n").lower()
    #for i in yes:
    if answer in yes:
        print(land_desc.instructions)
        
    else:
        print("Ahh, you already know how to play")



def new_player():
    player=input("\nLets get you setup with our outfitter.\n\nWhat is the full name \
of your adventurer?\n")
    player_name.append(player)




#### --- LAND DEFINITIONS --- ####





def land_0(): # STARTING POINT...for now
    curr_land[:] = [0]
    print(land_desc.land_0)
    answer=input(what_to_do).lower()
    if answer in west:
        prev_land[:] = [0]
        land_1()
    elif answer in east:
        prev_land[:] = [0]
        land_2()
    elif answer in south:
        prev_land[:] = [0]
        land_11()    
    elif answer in leave_game:
        leave_game_now()
    elif answer == "db":
        print("\n\n", db, "\n\n")
        land_0()
    else:
        land_0()


def land_1(): # ALONG THE RIVER
    curr_land[:] = [1]
    print(land_desc.land_1)
    answer=input(what_to_do).lower()
    if answer in east:
        prev_land[:] = [1]
        land_0()
    elif answer in north:
        prev_land[:] = [1]
        land_3()
    elif answer in leave_game:
        leave_game_now()
    elif answer == "db":
        print("\n\n", db, "\n\n")
        land_1()
    else:
        land_1()
        
        
def land_2(): # MOUNTAINOUS OVERLOOK
    curr_land[:] = [2]
    print(land_desc.land_2)
    answer=input(what_to_do).lower()
    if answer in west:
        prev_land[:] = [2]
        land_0()
    elif answer in leave_game:
        leave_game_now()
    elif answer == "db":
        print("\n\n", db, "\n\n")
        land_2()
    else:
        land_2()


def land_3(): # DARK FOREST
    curr_land[:] = [3]
    print(land_desc.land_3)
    answer=input(what_to_do).lower()
    if answer in north:
        prev_land[:] = [3]
        land_6()
    elif answer in east:
        prev_land[:] = [3]
        land_4()
    elif answer in south:
        prev_land[:] = [3]
        land_1()
    elif answer in leave_game:
        leave_game_now()
    elif answer == "db":
        print("\n\n", db, "\n\n")
        land_3()
    else:
        land_3()


def land_4(): # MUSHROOM HOUSE
    curr_land[:] = [4]
    print(land_desc.land_4)
    answer=input(what_to_do).lower()
    if answer in north:
        prev_land[:] = [4]
        land_5()
    elif answer in west:
        prev_land[:] = [4]
        land_3()
    elif answer in leave_game:
        leave_game_now()
    elif answer.startswith("enter") and answer.endswith("house"):
        prev_land[:] = [4]
        land_4_house_0()
    elif answer.startswith("look") and answer.endswith("house"):
        prev_land[:] = [4]
        print(land_4_desc_house_outside)
    elif answer in leave_game:
        leave_game_now()
    elif answer == "db":
        print("\n\n", db, "\n\n")
        land_4()
    else:
        land_4()
        

def land_4_house_0(): 
    curr_land[:] = [40]
    print(land_desc.land_4_house_0)
    answer=input(what_to_do).lower()
    if answer in west:
        prev_land[:] = [40]
        land_4_house_1()
    elif answer in east:
        prev_land[:] = [40]
        land_4_house_2()
    elif answer in south:
        prev_land[:] = [40]
        land_4()
    elif answer in leave_game:
        leave_game_now()
    else:
        land_4_house_0()

def land_4_house_1():
    curr_land[:] = [41]
    print(land_desc.land_4_house_1)
    answer=input(what_to_do).lower()
    if answer in east:
        prev_land[:] = [41]
        land_4_house_0()
    elif answer in leave_game:
        leave_game_now()
    else:
        land_4_house_1()

def land_4_house_2():
    curr_land[:] = [42]
    print(land_desc.land_4_house_2)
    answer=input(what_to_do).lower()
    if answer in north:
        prev_land[:] = [42]
        land_4_house_3()
    elif answer in east:
        prev_land[:] = [42]
        land_4_house_0()
    elif answer in leave_game:
        leave_game_now()
    else:
        land_4_house_2()

def land_4_house_3():
    curr_land[:] = [43]
    print(land_desc.land_4_house_3)
    answer=input(what_to_do).lower()
    if answer in south:
        prev_land[:] = [42]
        land_4_house_2()
    elif answer in leave_game:
        leave_game_now()
    else:
        land_4_house_3()


def land_5(): # FAIRY GARDEN
    curr_land[:] = [5]
    print(land_desc.land_5)
    answer=input(what_to_do).lower()
    if answer in west:
        prev_land[:] = [5]
        land_6()
    elif answer in south:
        prev_land[:] = [5]
        land_4()
    elif answer.startswith("talk") and answer.endswith("fairy"):
        talk_fairy_0()
    elif answer in leave_game:
            leave_game_now()
    else:
        land_5()
        

def land_6(): # EDGE OF DARK FOREST
    curr_land[:] = [6]
    print(land_desc.land_6)
    answer=input(what_to_do).lower()
    if answer in west:
        prev_land[:] = [6]
        land_7()
    elif answer in east:
        prev_land[:] = [6]
        land_5()
    elif answer in south:
        prev_land[:] = [6]
        land_3()
    elif answer in leave_game:
        leave_game_now()
    else:
        land_6()


def land_7(): # NOT SURE YET
    curr_land[:] = [7]
    print(land_desc.land_7)
    answer=input(what_to_do).lower()
    if answer in west:
        prev_land[:] = [7]
        land_10()
    elif answer in east:
        prev_land[:] = [7]
        land_6()
    elif answer in south:
        prev_land[:] = [7]
        land_8()
    elif answer in leave_game:
        leave_game_now()
    else:
        land_7()


def land_8(): # LAKE
    curr_land[:] = [8]
    print(land_desc.land_8)
    answer=input(what_to_do).lower()
    if answer in north:
        prev_land[:] = [8]
        land_7()
    elif answer in west:
        prev_land[:] = [8]
        land_9()
    elif answer in leave_game:
        leave_game_now()
    else:
        land_8()
        
        
def land_9(): # WILD FLOWER PRAIRIE
    curr_land[:] = [9]
    print(land_desc.land_9)
    answer=input(what_to_do).lower()
    if answer in north:
        prev_land[:] = [9]
        land_10()
    elif answer in east:
        prev_land[:] = [9]
        land_8()
    elif answer in leave_game:
        leave_game_now()
    else:
        land_9()
        

def land_10(): # PINE FOREST
    curr_land[:] = [10]
    print(land_desc.land_10)
    answer=input(what_to_do).lower()
    if answer in east:
        prev_land[:] = [10]
        land_7()
    elif answer in south:
        prev_land[:] = [10]
        land_8()
    elif answer in leave_game:
        leave_game_now()
    else:
        land_10()

def land_11():
    curr_land[:] = [11]
    print(land_desc.land_11)
    answer=input(what_to_do).lower()
    if answer in north:
        prev_land[:] = [11]
        land_0()
    elif answer in leave_game:
        leave_game_now()
        land_11()
    elif answer in pl_inv:
        print(display_inv)
        land_11()
    elif answer.startswith("enter") and answer.endswith("my car"):
        print(land_desc.land_11_ending)
        quit()    
    elif answer.startswith("look") and answer.endswith("map"):
        print(land_desc.land_map)
        land_11()    
    elif answer.startswith("look") and answer.endswith("sign"):
        print(land_desc.land_11_sign)
        land_11()
    elif answer.startswith("look") and answer.endswith("tree"):
        print(land_desc.land_11_tree)
        land_11()
    elif answer == "db":
        print("\n\n", db, "\n\n")
        land_11()
    else:
        land_11()        



#def land_12 # SECRET CAVE
        
def talk_fairy_0():
    print("""\nYou open your mouth to speak, yet no words come out.
    They seem to be busy at the moment\n""")
    land_5()
    


def c_l():
    c_la = curr_land
    for l in c_la:
        if l == 0:
            land_0()
        elif l == 1:
            land_1()
        elif l == 2:
            land_2()
        elif l == 3:
            land_3()
        elif l == 4:
            land_4()
        elif l == 40:
            land_40()
        elif l == 41:
            land_41()
        elif l == 42:
            land_42()
        elif l == 43:
            land_43()
        elif l == 5:
            land_5()
        elif l == 6:
            land_6()
        elif l == 7:
            land_7()
        elif l == 8:
            land_8()
        elif l == 9:
            land_9()
        elif l == 10:
            land_10()
        elif l == 11:
            land_11()
    #elif curr_grid == 12:
    #   land_12()
    else:
        print("not working")




#### ---- END ---- ####




#### ---- PROGRAM RUN CODE ---- ####



greet()
new_player()
print("Hey,", player_name[0], "\n")
#startup()
print(land_desc.land_11_start)
land_11()






#### ---- END RUN CODE ---- ####










#### ---- EOF ---- ####
