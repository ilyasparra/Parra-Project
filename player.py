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
    def game_loop(Player):
        while Player.move_count < 10:
            next_loc = Player.choose()
            Player.move(next_loc)
            Player.move_count += 1
    def ending(Player):
        if Quit_Status:
            Player.move(11)
        else:
            Player.move(12)
        