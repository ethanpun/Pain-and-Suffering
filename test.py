#test
# from main import game

import data
import game

# test = game.MUDGame()

def test():

    # try:
    #     data.start_menu()
    # except:
    #     print("Start Menu is screwed")
    # else:
    #     print("Start Menu is fine")

    try:
        test_spawn_room = data.start_room()
        print(test_spawn_room)
    except:
        print("i can't spawn cuz the room is bugged")
    
    # try:
    #     test.run()
    # except:
    #     print("The game cannot run lmao.")


    
test()
