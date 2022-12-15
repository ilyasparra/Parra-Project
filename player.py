from general_info import*
import general_info
from location import Location
from world import World
class Player:
    Current_Save_Data = ""
    def __init__(Player):
        Player.name = ""
        Player.world = World()
        Player.current_locale = 0
        Player.locations_visited = []
        Player.move_count = 0
        Player.score = 0
    def get_info(Player,type):
        if type == "NAME":
            return Player.name
        elif type == "MOVE_CNT":
            return Player.move_count
        elif type == "SCORE":
            return Player.score
    def update_save_data(Player,reset=False):
        if reset:
            general_info.Current_Save_Data = ""
            return None
        name = "Name: " + Player.name
        current_location = "Location: " + str(Player.current_locale)
        locations_visited = "Locations_Visited: " + str(Player.locations_visited)
        moves = "Moves_Done: " + str(Player.move_count)
        score = "Score: " + str(Player.score)
        Data = name + "\n" + current_location + "\n" + locations_visited + "\n" + moves + "\n" + score + "\n"
        general_info.Current_Save_Data = Data
        return None
    def load_save_data(Player):
        save_data = general_info.Load_Data.get("Save_Data")
        Player.name = save_data.get("Name")
        Player.current_locale = save_data.get("Location_Id")
        Player.locations_visited = save_data.get("Locations_Visited")
        for location in Player.world.Location_List:
            if location.id in Player.locations_visited:
                location.set_visited(True)
            else:
                location.set_visited(False)
        Player.move_count = save_data.get("Moves_Done")
        Player.score = save_data.get("Score")
        general_info.Load_Data["Load_Status"] = False
        Location_Name = general_info.Locations_Dict[Player.current_locale].get("Name")
        print(f"\nNew Game Loaded. Current Location is {Location_Name}")
        input("\nPress Enter to continue")
    def set_name(Player,str):
        Player.name = str
    def start(Player):
        Player.current_locale = 0
        Player.world.Location_Initialization()
        Player.world.update_location("SETUP")
        Player.set_name(general_info.Name)
    def move(Player,id):
        Player.move_count += 1
        Player.current_locale = id
        Player.locations_visited.append(id)
        Player.update_save_data()
        Player.world.update_location(id)
    def choose(Player):
        user_choice = Player.world.options(Player.current_locale)
        return user_choice
    def setup(Player):
        Player.start()
        Player.move(7)
    def progress_display(Player):
        if Player.current_locale >=1 and Player.current_locale <= 10:
            loc_name = Locations_Dict[Player.current_locale].get("Name")
            loc_status = Locations_Dict[Player.current_locale].get("Was_Visited")
            if not loc_status:
                Player.score += 25
                Locations_Dict[Player.current_locale]["Was_Visited"] = True
            print(f"\nYou have just visited {loc_name}\nNice Job!\nYour score is now {Player.score}")
    def game_loop(Player):
        while Player.move_count < 10 and not general_info.Quit_Status and not general_info.Load_Data.get("Load_Status"):
            Player.progress_display()
            next_loc = Player.choose()
            Player.move(next_loc)
            Player.move_count += 1
    def ending(Player):
        Player.progress_display()
        if general_info.Quit_Status:
            Player.move(11)
        elif general_info.Load_Data.get("Load_Status"):
            Player.load_save_data()
            Player.game_loop()
        else:
            Player.move(12)
        