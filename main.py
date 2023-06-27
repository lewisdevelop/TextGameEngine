
class User:
    health = 100
    inventory = {}
    money = 0
    name = "Player Name Here"


def prompt(options:list, topDialog:str, bottomPrompt:str, functionsList:list, arguements:list):
    print(topDialog)
    print("\n")
    optionsDict = {}
    for i in range(len(options)):
        print(f"[{i+1}] {options[i]}")
        optionsDict[i+1] = i+1
    print("\n")
    output = int(input(bottomPrompt))
    for x in range(len(optionsDict)):
        if output == optionsDict[x+1]:
            return functionsList[x](arguements=arguements)

def userModify(usrclass, changeDataName, changeData, changeDataNameINV):
    if changeDataName == "name":
        usrclass.name = changeData
    elif changeDataName == "money":
        usrclass.money = changeData
    elif changeDataName == "Inventory":
        usrclass.inventory[changeDataNameINV] = changeData
    else:
        print("Sorry! Custom User Data is currently a WIP!")

def manageArguements(listofArgs:list, need:int):
    for i in range(len(listofArgs)):
        if i == need:
            return listofArgs[i]