# Trip to England 
# Welcome to your free trip to England! 
#You are an aspiring soccer player and got invited to visit each stadium for every top soccer team in the Premier League! 
import random
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
msg_1 = "Press enter to continue:"
msg_2 = "You are at Old Trafford surrounded by red jerseys of Manchester United fans."
msg_3 = "You are at the Etihad surrounded by Manchester City fans."
msg_4 = "You are currently at Villa Park surrounded by Aston Villa fans."
msg_5 = "You are standing in front of the Emirates in front of plenty of Arsenal fans."
msg_6 = "You gaze upon Anfield with Liverpool fans around you."
msg_7 = "You visit the King Power Staidum surrounded by Leicester City fans"
msg_8 = "You are at Stamford Bridge with the loud Chelsea fans."
msg_9 = "You are at the well known Goodison Park with Everton fans."
msg_10 = "You have reached Selhurst Park, the stadium for Crystal Palace."
msg_11 = "You are at the home of West Ham United, London Stadium."
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


def MiniStop_Printer(inp,out):
    global m_cnt
    m = input(f"{inp}")
    Command_Check(m)
    m_cnt = m_cnt + 1
    print(f"{out}")
def Begin(msg=begin):
    global cnt
    if  cnt == 1:
        msg = msg_1
    elif cnt == 11:
        msg = end
    b = input(f"{msg}\n")
    Command_Check(b)
    
def Message_Printer(m):
    global user_name
    if not m == Game_Title:
        print(f"{m}")
    else:
        print(f"{m}")
        user_name = input("Enter your name: ")
        print(f"Hey, {user_name}! Hope you are doing well. Guess what? Congratulations, because of your hard work and dedication playing soccer, you have been awarded a free trip to England!")
def Progress_Display():
    global cnt
    print(f"You are at stop number {cnt}")
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
def main():
    global cnt,m_cnt,msg_1,Quit_Status,ending_text,copyright_text
    for i in range(Game_Loop_Cnt):
        if i == 0:
            Count_Update()
            Message_Printer(Game_Msg_List[i])
            Progress_Display()
            Begin()
        else:
            if Quit_Status:
                break
            else:
                Message_Printer(Game_Msg_List[i])    
                Count_Update()
                Progress_Display()
                MiniStop_Printer(Game_Ministop_List[i-1][0],Game_Ministop_List[i-1][1])
                Begin()
    if not Quit_Status:
        ending_text =  "Thank you, " + user_name + " for playing this game!"
        print(ending_text)
        print(copyright_text)
        print(f"Your total amount of stops were: {cnt}")
        print()
        print("Goodbye")
    elif Quit_Status:
        print("You quit the game early :(")
        ending_text =  "Thank you, " + user_name + " for playing this game!"
        print(ending_text)
        print(copyright_text)
        print(f"Your total amount of stops were: {cnt}")
        print("Goodbye, next time complete the game.")
        
main()