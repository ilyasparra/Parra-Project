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
User_Commmands = ["","NORTH","SOUTH","EXAMINE","HELP","QUIT"]
Examine_Statements = ["Nice","full of Loud people","Colorful","A Competitve place"]
Map = [
    ["N",4,2,6],
    [1,8,7,9],
    ["N",5,10,3]
]