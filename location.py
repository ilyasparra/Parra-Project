from general_info import*
import general_info
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
    def set_visited(Location,status=True):
        if status:
            general_info.Locations_Dict[Location.id]["Was_Visited"] = True
            Location.visited_status = True
        else:
            general_info.Locations_Dict[Location.id]["Was_Visited"] = False
            Location.visited_status = False
    def id_by_name(name):
            ans = -1
            for i in range(1,11):
                if Locations_Dict[i].get("Name") == name:
                    ans = i
                    return ans
            return ans
    def user_command(Location,str):
        def recur():
            recur_str = input("Press Enter to continue or input another command: ")
            Location.user_command(recur_str)
        continue_msg = "\nPress enter to continue"
        command_id = general_info.User_Command_Finder(str)
        if command_id == 0 or command_id == "Not Found":
            # Space to continue
                pass
        elif command_id == 1:
            # North
            coords = id_to_coords(Location.id)
            locale = get_nearby_locations(coords)[0]
            print(Location_List_General[locale])
            recur()
            pass
        elif command_id == 2:
            # South
            coords = id_to_coords(Location.id)
            locale = get_nearby_locations(coords)[1]
            print(Location_List_General[locale])
            recur()
        elif command_id == 3:
            # East
            coords = id_to_coords(Location.id)
            locale = get_nearby_locations(coords)[2]
            print(Location_List_General[locale])
            recur()
        elif command_id == 4:
            # West
            coords = id_to_coords(Location.id)
            locale = get_nearby_locations(coords)[3]
            print(Location_List_General[locale])
            recur()
        elif command_id == 5:
            # Examine
            print(Location)
            recur()
            pass
        elif command_id == 6:
            # Help
            print(general_info.Help)
            recur()
            pass
        elif command_id == 7:
            general_info.Quit_Status = True
            print(general_info.Quit_Msg)
            recur()
            pass
        elif command_id == 8:
            # Save
            save_file_name = prompt_save_name("WRITE")
            save_file = open(save_file_name,"w")
            save_file.write(general_info.Current_Save_Data)
            save_file.close()
            print("Save file has been created")
            recur()
        elif command_id == 9:
            # Load
            save_file_name = prompt_save_name("READ")
            save_data = read_save_file(save_file_name)
            general_info.Load_Data["Save_Data"] = save_data
            general_info.Load_Data["Load_Status"] = True
            print("New save file will be loaded upon current location's completion.")
            recur()
    def play_location(Location):
        if Location.id != 0 and Location.id <= 10:
            print("\n"+Location.message)
            user_input = input("\n"+Location.input)
            Location.user_command(user_input)
            if Location.output != None:
                user_input = input("\n"+Location.output)
                Location.user_command(user_input)
        elif Location.id == 0:
            print("\n"+Location.message)
            name_set = input("\n"+Location.info.get("Name_Set"))
            general_info.Name = name_set
            print("\n"+Location.info.get("Greeting"))
            input("\n"+Location.input)
        else:
            print("\n"+Location.message)
            print("\nThank you for playing this game!")
            input("\n"+Location.input)

