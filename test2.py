User_Commmands = ["","NORTH","SOUTH","WEST","EAST","Examine","HELP","QUIT"]
def Index_Func(s):
    for i in range(len(User_Commmands)):
        if s.upper() == User_Commmands[i]:
            return i
    return -1
print(Index_Func("North"))