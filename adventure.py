# Trip to England 
# Welcome to your free trip to England! 
#You are an aspiring soccer player and got invited to visit each stadium for every top soccer team in the Premier League! 
cnt = 0
m_cnt = 0
msg_1 = "Press enter to continue:"
msg_2 = "You are at Old Trafford surrounded by red jerseys of Manchester United fans."
msg_3 = "You are at the Etihad surrounded by Manchester City fans."
msg_4 = "You are currently at Villa Park surrounded by Aston Villa fans."
msg_5 = "You are standing in front of the Emirates in front of plenty of Arsenal fans."
msg_6 = "You gaze upon Anfield with Liverpool fans around you."
msg_7 = "You visit the King Power Staidum surrounded by Leicester City fans"
msg_8 = "You are at Stamford Bridge with the loud Chelsea fans."
msg_9 = "You are at the well known Goodison Park with Everton fans."
msg_10 = "You have reached Selhurst Park, the stadium for Crystal Palace."
msg_11 = "You are at the home of West Ham United, London Stadium."
def main():
    global cnt,m_cnt,msg_1
    
    cnt = cnt + 1

    print(f"You are at stop number {cnt}")
    begin = input(f"{msg_1}")
    print(begin)

    print(f"{msg_2}")
    cnt = cnt + 1
    print(f"This is stop number {cnt}")

    ministop1 = input("Press enter to buy a jersey: ")
    m_cnt = m_cnt + 1
    print("The jersey is red and super nice.")

    begin1 = input("Press enter to continue to the next stadium: ")
    
    print(begin1)

    print(" ")

    print(f"{msg_3}")
    cnt = cnt + 1 
    print(f"This is stop number {cnt}")

    ministop2 = input("Press enter to buy a scarf: ")
    m_cnt = m_cnt + 1
    print("The light blue scarf keeps you really warm.")
    
    begin2 = input("Press enter to continue to the next stadium ")

    print(begin2)

    print(f"{msg_4}")
    cnt = cnt + 1 
    print(f"This is stop number {cnt}")
    
    ministop3 = input("Press enter to buy a burger.")
    m_cnt = m_cnt + 1
    print("The burger was too overpriced, note to self, do not ever buy a burger in England again.")
    
    begin3 = input("Press enter to continue to the next stadium: ")

    print(begin3)

    print(f"{msg_5}")
    cnt = cnt + 1 
    print(f"This is stop number {cnt}")
    
    ministop4 = input("Press enter to learn about one of Arsenal's best players: ")
    m_cnt = m_cnt + 1
    print("The player is Mesut Ozil, he was an attacking oriented midfielder, he was amazing!")
    
    begin4 = input("Press enter to continue to the next stadium: ")

    print(begin4)

    print(f"{msg_6}")
    cnt = cnt + 1 
    print(f"This is stop number {cnt}")
    
    ministop4 = input("Press enter to learn a Liverpool chant: ")
    m_cnt = m_cnt + 1
    print("Walk on, walk on, With hope in your heart, And you'll never walk alone, You'll NEVER walk alone!!!")
    
    begin5 = input("Press enter to continue to the next stadium: ")

    print(begin5)

    print(f"{msg_7}")
    cnt = cnt + 1 
    print(f"This is stop number {cnt}")

    ministop4 = input("Press enter to learn a fact about Leicester City: ")
    m_cnt = m_cnt + 1
    print("Leicester City made an astonishing comeback to win the Premier League in 2016.")

    begin6 = input("Press enter to continue to the next stadium: ")

    print(begin6)

    print(f"{msg_8}")
    cnt = cnt + 1 
    print(f"This is stop number {cnt}")

    ministop4 = input("Press enter to learn about a fantastic player at Chelsea: ")
    m_cnt = m_cnt + 1
    print("The player is Eden Hazard he was an attacking forward at Chelsea and was considered one of the best players in the world at one point!")

    begin7 = input("Press enter to continue to the next stadium: ")

    print(begin7)

    print(f"{msg_9}")
    cnt = cnt + 1
    print(f"This is stop number {cnt}")

    ministop4 = input("Press enter to buy Everton gloves: ")
    m_cnt = m_cnt + 1
    print("The gloves keep your hands warm and they allow you to use your phone to take picutres or videos.")

    begin8 = input("Press enter to continue to the next stadium: ")

    print(begin8)

    print(f"{msg_10}")
    cnt = cnt + 1 
    print(f"This is stop number {cnt}")
    
    ministop4 = input("Press enter to learn about a Crystal Palace player: ")
    m_cnt = m_cnt + 1
    print("The player is Wilfried Zaha, he is an extremely skillful attacking player at Crystal Palace.")
    
    begin9 = input("Press enter to continue to the next stadium: ")

    print(begin9)

    print(f"{msg_11}")
    cnt = cnt + 1 
    print(f"This is stop number {cnt}")
    
    print(" ")

    ministop4 = input("Press enter to purchase a Premier League Trophy: ")
    m_cnt = m_cnt + 1
    print("The trophy was a replica, therefore it was very expensive, but worth the flex that own it.")

    begin10 = input("You have finished your trip!")

    print(begin10)

    print("Thank you")
    print(f"Your total amount of stops were: {cnt}")
    print("Goodbye")

main()


