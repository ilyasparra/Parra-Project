from general_info import*
from location import Location
from world import World
class Player:
    def __init__(Player):
        Player.name = ""
        Player.world = World()
        Player.current_locale = Player.world.get_current_location()
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
    def move(Player):
        Player.world.Location_Sequence()
        pass
        