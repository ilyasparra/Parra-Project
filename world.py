from general_info import Map,Locations_Dict, Quit_Status
from location import Location
class World:
    Location_List = []
    map = []
    def __init__(World):
        World.Location_Initialization()
        World.Move_Limit = 10
        World.map = Map
        World.current_location = 0
        World.setup = True
        pass
    def get_surrounding_locations(World,coords,):
        r, c = coords
        North_offset = [-1,0]
        South_offset = [1,0]
        East_offset = [0,1]
        West_offset = [0,-1]
        if r == 0:
            North_offset = [0,0]
        elif r == len(World.map)-1:
            South_offset = [0,0]
        if c == 0:
            East_offset = [0,0]
        elif c == len(World.map[r])-1:
            West_offset = [0,0]
        offsets = [North_offset,South_offset,East_offset,West_offset]
        surrounding_locations = [[],[],[],[]] # North, South, East, West
        for offset in offsets:
            new_coords = coords
            new_coords[0] += offset[0]
            new_coords[1] += offset[1]
            surrounding_locations[offset] = new_coords
        return surrounding_locations
    def get_coords(World,id):
        map_coords = [None,None]
        Break_Indicator = False
        for row in World.map:
            for col in World.map:
                if World.map[row][col] == id:
                    map_coords = row, col
                    Break_Indicator = True
                    break
            if Break_Indicator:
                break
            return map_coords
        pass
    def options(World):
        # find current location map coords
        map_coords = World.get_coords(World.current_location)
        row, col = map_coords
        # Find surrounding locations
        surrounding_locations = World.get_surrounding_locations(map_coords)
        # Filter out eligible locations
        for s_loc in surrounding_locations:
            nearby_loc = World.map[s_loc[0]][s_loc[1]]
            current_loc = World.map[row][col]
            if nearby_loc == "N" or nearby_loc == current_loc:
                s_loc = "NA"
            else:
                num_id = World.map[row][col]
                s_loc[0] = num_id
                s_loc[1] = Locations_Dict[num_id].get("Name")
        # Get names and prepare strings
        North = f"\nNorth of you is {surrounding_locations[0][1]} "
        South = f"\nSouth of you is {surrounding_locations[1][1]} "
        East =  f"\nEast of you is {surrounding_locations[2][1]} "
        West =  f"\nWest of you is {surrounding_locations[3][1]} "
        Directions = [North,South,East,West]
        # Display options
        options:str = ""
        for status in surrounding_locations:
            if not status[1] == "NA":
                index = surrounding_locations.index(status)
                options = options + Directions[index]
            options = options +"\n"
        user_choice = input(f"\nSurrounding Destinations:\n{options}\nPress Enter to replay the location or\nChoose a cardinal direction to move to: ")
        # Act on user response and return appropriate location id
        for name in surrounding_locations:
            if not user_choice.find(name[1]) == -1:
                loc_id = name[0]
                return loc_id
            else:
                print("\nReplaying previous stadium due to invalid command or enter key\n")
                return World.map[row][col]
    def Location_Sequence(World):
        Player_Location = World.Location_List[World.current_location]
        if World.setup:
            Player_Location.play_location()
            World.current_location = 1
        while World.Move_Limit > 0 and not Quit_Status:
            Player_Location.play_location()
            World.current_location = World.options()
            World.Move_Limit -= 1
        if Quit_Status:
            World.current_location = 11 # 11 is for quit ending
            Player_Location.play_location()
        else:
            World.current_location = 12 # 12 is for finish ending
            Player_Location.play_location()
    def Location_Initialization(World):
        for id in range(10):
            World.Location_List.append(Location(id))
 


    