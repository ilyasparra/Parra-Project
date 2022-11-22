from general_info import Map,Locations_Dict, Quit_Status, get_nearby_locations, id_to_coords,Location_List_General
from location import Location
class World:
    Location_List = []
    map = []
    def __init__(World):
        World.Move_Limit = 10
        World.map = Map
        World.current_location:int
        World.setup = True
        pass
    def get_current_location(World):
        return World.current_location
    def get_surrounding_locations(World,coords):
        surrounding_locations = get_nearby_locations(coords)
        return surrounding_locations
    def get_coords(World,id):
        coords = id_to_coords(id)
        return coords
    def options(World,id):
        # find current location map coords
        map_coords = World.get_coords(id)
        row, col = map_coords
        # Find surrounding locations
        surrounding_locations = World.get_surrounding_locations(map_coords)
        # Filter out eligible locations
        Info = []
        for s_loc in surrounding_locations:
            nearby_loc = World.map[s_loc[0]][s_loc[1]]
            current_loc = World.map[row][col]
            arr = [None,None]
            if nearby_loc == "N" or nearby_loc == current_loc:
                arr[0] = "NA"
                arr[1] = "NA"
            else:
                num_id = World.map[s_loc[0]][s_loc[1]]
                arr[0] = num_id
                arr[1] = Locations_Dict[num_id].get("Name")
            Info.append(arr)
        # Get names and prepare strings
        North = f"\nNorth of you is {Info[0][1]} "
        South = f"\nSouth of you is {Info[1][1]} "
        East =  f"\nEast of you is {Info[2][1]} "
        West =  f"\nWest of you is {Info[3][1]} "
        Directions = [North,South,East,West]
        # Display options
        options:str = ""
        for name in Info:
            if not name[1] == "NA":
                index = Info.index(name)
                str = Directions[index] + "\n"
                options = options + str
        user_choice = input(f"\nSurrounding Destinations:\n{options}\nPress Enter to replay the location or\nChoose a cardinal direction to move to: ")
        # Act on user response and return appropriate location id
        for name in Info:
            if user_choice.find(name[1]) != -1:
                loc_id = name[0]
                return loc_id
            
        print("\nReplaying previous stadium due to invalid command or enter key\n")
        return World.map[row][col]
    def update_location(World,id):
        if id == "SETUP":
            World.current_location = 0
        else:
            World.current_location = id
        player_locale = World.Location_List[World.current_location]
        player_locale.play_location()
        pass
    def Location_Initialization(World):
        for id in range(len(Locations_Dict)):
            World.Location_List.append(Location(id))
            Location_List_General.append(Location(id))
 

