from general_info import*
from location import Location
from world import World
class Player:
    def __init__(Player):
        Player.name = ""
        Player.world = World()
        Player.current_locale = 0
        Player.move_count = 0
        Player.score = 0
    def get_info(Player,type):
        if type == "NAME":
            return Player.name
        elif type == "MOVE_CNT":
            return Player.move_count
        elif type == "SCORE":
            return Player.score
    def set_name(Player,str):
        Player.name = str
    def start(Player):
        Player.current_locale = 0
        Player.world.Location_Initialization()
        Player.world.update_location("SETUP")
        Player.set_name
    def move(Player,id):
        Player.current_locale = id
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
            print(f"\nYou have just visited + {loc_name}\nNice Job!\nYour score is now {Player.score}")
    def game_loop(Player):
        while Player.move_count < 10:
            Player.progress_display()
            next_loc = Player.choose()
            Player.move(next_loc)
            Player.move_count += 1
    def ending(Player):
        Player.progress_display()
        if Quit_Status:
            Player.move(11)
        else:
            Player.move(12)
        