from general_info import Locations_Dict,Examine_Statements,User_Commmands,Help,Quit_Status,Quit_Msg,id_to_coords,get_nearby_locations,Location_List_General,Name
import random
class Location:
    def __init__(Location,id):
        Location.id = id
        Location.info = Locations_Dict[Location.id]
        Location.name = Location.info.get("Name")
        Location.message = Location.info.get("Message")
        Location.input = Location.info.get("Input_Text")
        Location.output = Location.info.get("Output_Text") 
        Location.visited_status = Location.info.get("Was_Visited")
    def __str__(Location):
        str = ""
        if Location.visited_status:
            str = "You are at " + Location.name
        else:
            str = "This place is " + Examine_Statements[random.randint(0,len(Examine_Statements)-1)]
        return str
    def get(Location,type):
        if type == "Name":
            return Location.name
        elif type == "Message":
            return Location.message
        elif type == "Input":
            return Location.input
        elif type == "Output":
            return Location.output
        pass
    def set_visited(Location):
        Locations_Dict[Location.id]["Was_Visited"] = True
        Location.visited_status = True
    def id_by_name(name):
            ans = -1
            for i in range(1,11):
                if Locations_Dict[i].get("Name") == name:
                    ans = i
                    return ans
            return ans
    def user_command(Location,str):
        continue_msg = "\nPress enter to continue"
        if not Location.name != None:
            if str.find(User_Commmands[0]) != -1:
                pass
            elif str.upper().find(User_Commmands[1]) != -1:
                coords = id_to_coords(Location.id)
                locale = get_nearby_locations(coords)[0]
                print(Location_List_General[locale])
                user_response = input(continue_msg)
                Location.user_command(user_response)
                pass
            elif str.upper().find(User_Commmands[2]) != -1:
                coords = id_to_coords(Location.id)
                locale = get_nearby_locations(coords)[1]
                print(Location_List_General[locale])
                user_response = input(continue_msg)
                Location.user_command(user_response)
            elif str.upper().find(User_Commmands[3]) != -1:
                coords = id_to_coords(Location.id)
                locale = get_nearby_locations(coords)[2]
                print(Location_List_General[locale])
                user_response = input(continue_msg)
                Location.user_command(user_response)
            elif str.upper().find(User_Commmands[4]) != -1:
                coords = id_to_coords(Location.id)
                locale = get_nearby_locations(coords)[3]
                print(Location_List_General[locale])
                user_response = input(continue_msg)
                Location.user_command(user_response)
            elif str.upper().find(User_Commmands[5]) != -1:
                print(Location)
                user_response = input(continue_msg)
                Location.user_command(user_response)
                pass
            elif str.upper().find(User_Commmands[6]) != -1:
                print(Help)
                user_response = input(continue_msg)
                Location.user_command(user_response)
                pass
            elif str.upper().find(User_Commmands[7]) != -1:
                Quit_Status = True
                print(Quit_Msg)
                user_response = input(continue_msg)
                Location.user_command(user_response)
                pass
    def play_location(Location):
        if Location.id != 0 and Location.id <= 10:
            print("\n"+Location.message)
            user_input = input("\n"+Location.input)
            Location.user_command(user_input)
            if Location.output != None:
                input("\n"+Location.output)
        elif Location.id == 0:
            print("\n"+Location.message)
            name_set = input("\n"+Location.info.get("Name_Set"))
            Name = name_set
            print("\n"+Location.info.get("Greeting"))
            input("\n"+Location.input)
        else:
            print("\n"+Location.message)
            print("\nThank you for playing this game!")
            input("\n"+Location.input)

