from world import World
from location import Location
from player import Player

def main():
    Player_Ins = Player()
    Player_Ins.setup()
    Player_Ins.game_loop()
    Player_Ins.ending()
main()

