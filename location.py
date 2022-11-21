from general_info import Locations_Dict,Examine_Statements,User_Commmands,Help,Quit_Status,Quit_Msg
import random
from world import World
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
    def user_command(Location,str):
        continue_msg = "\nPress enter to continue"
        if str.upper().find(User_Commmands[0]):
            pass
        elif str.upper().find(User_Commmands[1]):
            coords = World.get_coords(Location.id)
            locale = World.get_surrounding_locations(coords)[0]
            print(World.Location_List[locale])
            user_response = input(continue_msg)
            Location.user_command(user_response)
            pass
        elif str.upper().find(User_Commmands[2]):
            coords = World.get_coords(Location.id)
            locale = World.get_surrounding_locations(coords)[1]
            print(World.Location_List[locale])
            user_response = input(continue_msg)
            Location.user_command(user_response)
        elif str.upper().find(User_Commmands[3]):
            coords = World.get_coords(Location.id)
            locale = World.get_surrounding_locations(coords)[2]
            print(World.Location_List[locale])
            user_response = input(continue_msg)
            Location.user_command(user_response)
        elif str.upper().find(User_Commmands[4]):
            coords = World.get_coords(Location.id)
            locale = World.get_surrounding_locations(coords)[3]
            print(World.Location_List[locale])
            user_response = input(continue_msg)
            Location.user_command(user_response)
        elif str.upper().find(User_Commmands[5]):
            print(Location)
            user_response = input(continue_msg)
            Location.user_command(user_response)
            pass
        elif str.upper().find(User_Commmands[6]):
            print(Help)
            user_response = input(continue_msg)
            Location.user_command(user_response)
            pass
        elif str.upper().find(User_Commmands[7]):
            Quit_Status = True
            print(Quit_Msg)
            user_response = input(continue_msg)
            Location.user_command(user_response)
            pass
    def play_location(Location):
        print(Location.message)
        user_input = input(Location.input)
        Location.user_command(user_input)
        print(Location.output)
        pass