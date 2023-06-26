def prompt(options:list, topDialog:str, bottomPrompt:str):
    print(topDialog)
    print("\n")
    for i in range(len(options)):
        print(f"[{i+1}] {options[i]}")
    print("\n")
    return input(bottomPrompt)