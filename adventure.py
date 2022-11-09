# Trip to England 
# Welcome to your free trip to England! 
#You are an aspiring soccer player and got invited to visit each stadium for every top soccer team in the Premier League! 

import random
Start = True
score = 0
Next_Stop = 1
user_name = ""
cnt = 0
m_cnt = 0
ending_text:str
copyright_text = "©Ilyas Foundation Incorporated"
Help = "Possible Commands:\nPress Enter without typing to continue\nNORTH to see what location is north of you\nSOUTH to see what location is south of you\nEXAMINE to find information on current location\nQUIT to end game\nHELP to see commands again"
Game_Title = "\nWelcome to Your Free Trip To England\n"
begin = "Press enter to continue to the next stadium: "
end = "You have finished your trip! Press Enter to see credits"
Quit_Msg = "You have decided to quit the game. You will be exited out of the game after completing the stop."
Quit_Status = False
msg_1 = "\nPress enter to continue:"
msg_2 = "\nYou are at Old Trafford surrounded by red jerseys of Manchester United fans."
msg_3 = "\nYou are at the Etihad surrounded by Manchester City fans."
msg_4 = "\nYou are currently at Villa Park surrounded by Aston Villa fans."
msg_5 = "\nYou are standing in front of the Emirates in front of plenty of Arsenal fans."
msg_6 = "\nYou gaze upon Anfield with Liverpool fans around you."
msg_7 = "\nYou visit the King Power Staidum surrounded by Leicester City fans"
msg_8 = "\nYou are at Stamford Bridge with the loud Chelsea fans."
msg_9 = "\nYou are at the well known Goodison Park with Everton fans."
msg_10 = "\nYou have reached Selhurst Park, the stadium for Crystal Palace."
msg_11 = "\nYou are at the home of West Ham United, London Stadium."
Locations = ["Old Trafford","Etihad","Villa Park","Emirates","Anfield","King Power", "Stanford Bridge","Goodison Park","Selhurst Parl","London Stadium"]
ministop1_input_text = "Press enter to buy a jersey: "
ministop1_output_text = "The jersey is red and super nice."
ministop2_input_text = "Press enter to buy a scarf: "
ministop2_output_text = "The light blue scarf keeps you really warm."
ministop3_input_text = "Press enter to buy a burger:"
ministop3_output_text = "The burger was too overpriced, note to self, do not ever buy a burger in England again."
ministop4_input_text = "Press enter to learn about one of Arsenal's best players: "
ministop4_output_text = "The player is Mesut Ozil, he was an attacking oriented midfielder, he was amazing!"
ministop5_input_text = "Press enter to learn a Liverpool chant: "
ministop5_output_text = "Walk on, walk on, With hope in your heart, And you'll never walk alone, You'll NEVER walk alone!!!"
ministop6_input_text = "Press enter to learn a fact about Leicester City: "
ministop6_output_text = "Leicester City made an astonishing comeback to win the Premier League in 2016."
ministop7_input_text = "Press enter to learn about a fantastic player at Chelsea: "
ministop7_output_text = "The player is Eden Hazard he was an attacking forward at Chelsea and was considered one of the best players in the world at one point!"
ministop8_input_text = "Press enter to buy Everton gloves: "
ministop8_output_text = "The gloves keep your hands warm and they allow you to use your phone to take picutres or videos."
ministop9_input_text = "Press enter to learn about a Crystal Palace player: "
ministop9_output_text = "The player is Wilfried Zaha, he is an extremely skillful attacking player at Crystal Palace."
ministop10_input_text = "Press enter to purchase a Premier League Trophy: "
ministop10_output_text = "The player is Wilfried Zaha, he is an extremely skillful attacking player at Crystal Palace."
ministop11_input_text = "Press enter to purchase a Premier League Trophy: "
ministop11_output_text = "The trophy was a replica, therefore it was very expensive, but worth the flex that own it."
User_Commmands = ["","NORTH","SOUTH","EXAMINE","HELP","QUIT"]
Examine_Statements = ["Nice","full of Loud people","Colorful","Competitve place"]
def Index_Func(s):
    for i in range(len(User_Commmands)):
        if s.upper() == User_Commmands[i]:
            return i
    return -1
def Command_Check(s):
    global msg_1
    global Quit_Status
    global cnt
    global Help
    global Quit_Msg
    global Locations
    x:str
    if Index_Func(s) == 1 and cnt > 3:
        print(f"North of this location is the {Locations[cnt-3]} stadium")
        x = input(f"{msg_1}\n")
        Command_Check(x)
    elif Index_Func(s) == 2 and cnt < 11:
        print(f"South of this location is the {Locations[cnt-1]} stadium")
        x = input(f"{msg_1}\n")
        Command_Check(x)
    elif Index_Func(s) == 3:
        #Finish Examine
        print(f"The stadium {Locations[cnt-2]} is {Examine_Statements[random.randrange(0,len(Examine_Statements))]}")
        x = input(f"{msg_1}\n")
        Command_Check(x)
    elif Index_Func(s) == 4:
        print(Help)
        x = input(f"{msg_1}\n")
        Command_Check(x)
    elif Index_Func(s) == 5:
        Quit_Status = True
        print(Quit_Msg)
        print(Quit_Status)
        #x = input(f"{msg_1}")
        #Command_Check(x)
def Find_Next_Stop():
    global Next_Stop
    Break_Indicator = False
    current_coords = [None,None]
    for i in range(len(Map)):
        for j in range(len(Map[i])):
            if Map[i][j] == Next_Stop:
                current_coords[0] = i
                current_coords[1] = j
                Break_Indicator = True
                break
        if Break_Indicator:
            break
        print(f"Coords: {Map[i][j]}\nRow {current_coords[0]}\nCol {current_coords[1]}")
        
    surrounding_coords = [[],[],[],[]]
    
  
    
    if current_coords[0] == 0 or Map[current_coords[0]-1][current_coords[1]] == "N":
        surrounding_coords[0] = "None"
    else:  
        #North
        surrounding_coords[0] = Locations_Dict[Map[current_coords[0]-1][current_coords[1]]]["Name"]
    if current_coords[0] == 2 or Map[current_coords[0]+1][current_coords[1]] == "N":
        surrounding_coords[1] = "None"
    else:  
        #South
        surrounding_coords[1] = Locations_Dict[Map[current_coords[0]+1][current_coords[1]]]["Name"]
    if current_coords[1] == 0 or Map[current_coords[0]][current_coords[1]-1] == "N":
        surrounding_coords[2] = "None"
    else: 
        #West 
        surrounding_coords[2] = Locations_Dict[Map[current_coords[0]][current_coords[1]-1]]["Name"]
    if current_coords[1] == 3 or Map[current_coords[0]][current_coords[1]+1] == "N":
        surrounding_coords[3] = "None"
    else: 
        #East
        surrounding_coords[3] = Locations_Dict[Map[current_coords[0]][current_coords[1]+1]]["Name"]
    print(surrounding_coords)
    North = f"\nNorth of you is {surrounding_coords[0]} "
    South = f"\nSouth of you is {surrounding_coords[1]} "
    West =  f"\nWest of you is {surrounding_coords[2]} "
    East =  f"\nEast of you is {surrounding_coords[3]} "
    Directions = [North,South,West,East]
    User_Options_Index = []
    options:str = ""
    for i in Directions:
        if not (surrounding_coords[Directions.index(i)] == "None"):
            options = options + i
            User_Options_Index.append(Directions.index(i))
    options = options + "\n"
    def check_options(num):
        ans = False
        for p in User_Options_Index:
            if num == p:
                ans = True
        return ans 
    user_choice = input(f"\nSurrounding Destinations:\n{options}\nPress Enter to replay the location or\nChoose a cardinal direction to move to: ")
    User_Reponses = [["North",[-1,0]],["South",[1,0]],["West",[0,-1]],["East",[0,1]]]
    Found = False
    
    for j in User_Reponses:
        if not (user_choice.find(j[0]) == -1) and (check_options(User_Reponses.index(j))):
            next_location_id = Map[current_coords[0]+j[1][0]][current_coords[1]+j[1][1]]
            Next_Stop = next_location_id
            Found = True
            break
    if not Found:
        print("\nReplaying previous stadium due to invalid command or enter key\n")
        
            
    

def MiniStop_Printer(inp,out):
    global m_cnt
    m = input(f"{inp}")
    Command_Check(m)
    m_cnt = m_cnt + 1
    print(f"{out}")

def Begin(msg=begin):
    global cnt,Start
    if  cnt == 1:
        msg = msg_1
    elif cnt == 11:
        msg = end
    user_response = input(f"{msg}\n")
    Command_Check(user_response)
    
def Message_Printer(m):
    global user_name
    if not m == Game_Title:
        print(f"{m}")
    else:
        print(f"{m}")
        user_name = input("Enter your name: ")
        print(f"Hey, {user_name}! Hope you are doing well. Guess what? Congratulations, because of your hard work and dedication playing soccer, you have been awarded a free trip to England!")
def Progress_Display(score_show = 0):
    global cnt, score
    print(f"You are at stop number {cnt}")

    if score_show == 1:
        score = score + 10
        print(f"You have visited a new stadium!\nYou now have a score of {score} points!")
def Count_Update():
    global cnt
    cnt = cnt + 1
Game_Loop_Cnt = 11
Game_Msg_List = [Game_Title,msg_2,msg_3,msg_4,msg_5,msg_6,msg_7,msg_8,msg_9,msg_10,msg_11]
Game_Ministop_List = [[ministop1_input_text,ministop1_output_text],
[ministop2_input_text,ministop2_output_text],
[ministop3_input_text,ministop3_output_text],
[ministop4_input_text,ministop4_output_text],
[ministop5_input_text,ministop5_output_text],
[ministop6_input_text,ministop6_output_text],
[ministop7_input_text,ministop7_output_text],
[ministop8_input_text,ministop8_output_text],
[ministop9_input_text,ministop9_output_text],
[ministop10_input_text,ministop10_output_text],
[ministop11_input_text,ministop11_output_text],]
Map = [
    ["N",4,2,6],
    [1,8,7,9],
    ["N",5,10,3]
]
Locations_Dict = {
    0 : {
        "Message" : Game_Msg_List[0],
        "Was_Visited" : False
    },
    1 : {
        "Name" : "Old Trafford",
        "Message" : Game_Msg_List[1],
        "Input_Text" : Game_Ministop_List[1][0],
        "Output_Text" : Game_Ministop_List[1][1],
        "Was_Visited" : False
    },
    2 : {
        "Name" : "Ethiad",
        "Message" : Game_Msg_List[2],
        "Input_Text" : Game_Ministop_List[2][0],
        "Output_Text" : Game_Ministop_List[2][1],
        "Was_Visited" : False
    },
    3 : {
        "Name" : "Villa Park",
        "Message" : Game_Msg_List[3],
        "Input_Text" : Game_Ministop_List[3][0],
        "Output_Text" : Game_Ministop_List[3][1],
        "Was_Visited" : False
    },
    4 : {
        "Name" : "Emirates",
        "Message" : Game_Msg_List[4],
        "Input_Text" : Game_Ministop_List[4][0],
        "Output_Text" : Game_Ministop_List[4][1],
        "Was_Visited" : False
    },
    5 : {
        "Name" : "Anfield",
        "Message" : Game_Msg_List[5],
        "Input_Text" : Game_Ministop_List[5][0],
        "Output_Text" : Game_Ministop_List[5][1],
        "Was_Visited" : False
    },
    6 : {
        "Name" : "King Power",
        "Message" : Game_Msg_List[6],
        "Input_Text" : Game_Ministop_List[6][0],
        "Output_Text" : Game_Ministop_List[6][1],
        "Was_Visited" : False
    },
    7 : {
        "Name" : "Stamford Bridge",
        "Message" : Game_Msg_List[7],
        "Input_Text" : Game_Ministop_List[7][0],
        "Output_Text" : Game_Ministop_List[7][1],
        "Was_Visited" : False
    },
    8 : {
        "Name" : "Goodison Park",
        "Message" : Game_Msg_List[8],
        "Input_Text" : Game_Ministop_List[8][0],
        "Output_Text" : Game_Ministop_List[8][1],
        "Was_Visited" : False
    },
    9 : {
        "Name" : "Selhurst Park",
        "Message" : Game_Msg_List[9],
        "Input_Text" : Game_Ministop_List[9][0],
        "Output_Text" : Game_Ministop_List[9][1],
        "Was_Visited" : False
    },
    10 : {
        "Name" : "London Stadium",
        "Message" : Game_Msg_List[10],
        "Input_Text" : Game_Ministop_List[10][0],
        "Output_Text" : Game_Ministop_List[10][1],
        "Was_Visited" : False
    }
}

def Game_Begin():
    Count_Update()
    Message_Printer(Locations_Dict[0]["Message"])
    Progress_Display()
    Begin()
def Story_Sequence(num):
    global Start
    Message_Printer(Locations_Dict[num]["Message"])    
    if Start:
        Start = False
    else:
        Count_Update()
        Progress_Display(1)
    MiniStop_Printer(Locations_Dict[num]["Input_Text"],Locations_Dict[num]["Output_Text"])
    Begin()
def Normal_Ending():
    ending_text =  "Thank you, " + user_name + " for playing this game!"
    print(ending_text)
    print(copyright_text)
    print(f"Your total amount of stops were: {cnt}")
    print()
    print("Goodbye")
def Quit_Ending():
    print("You quit the game early :(")
    ending_text =  "Thank you, " + user_name + " for playing this game!"
    print(ending_text)
    print(copyright_text)
    print(f"Your total amount of stops were: {cnt}")
    print("Goodbye, next time complete the game.")
def main():
    global cnt,m_cnt,msg_1,Quit_Status,ending_text,copyright_text,Next_Stop
    for i in range(Game_Loop_Cnt):
        if i == 0:
            Game_Begin()
        else:
            if Quit_Status:
                break
            else:
                # Replace with next stop when done
               Story_Sequence(Next_Stop)
               Find_Next_Stop()
    if not Quit_Status:
        Normal_Ending()
    elif Quit_Status:
       Quit_Ending()
        
main()