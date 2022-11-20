from general_info import Locations_Dict,Examine_Statements
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