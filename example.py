import main as TGE

mainUser = TGE.User
def startGame(arguements):
    manager = TGE.manageArguements
    mainUser.health = manager(arguements, 1)
    mainUser.money = manager(arguements, 2)
    mainUser.inventory = manager(arguements, 3)
    print("TestHere")
print(TGE.prompt())