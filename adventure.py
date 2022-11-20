# Trip to England 
# Welcome to your free trip to England! 
#You are an aspiring soccer player and got invited to visit each stadium for every top soccer team in the Premier League! 
from general_info import*
import random
Start = True
score = 0
Next_Stop = 1
user_name = ""
cnt = 0
m_cnt = 0
Game_Loop_Cnt = 11

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