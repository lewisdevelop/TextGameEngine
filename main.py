def prompt(options:list, topDialog:str, bottomPrompt:str, functionsList:list, arguements:int):
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
            return functionsList[x](round=arguements)
    