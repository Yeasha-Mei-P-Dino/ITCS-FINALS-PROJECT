#introduction to conditional statements

gold = 0
miner = input("\n\t Hi, what's your name: ")

isGold = input("\t Is the mineral gold? ")

if isGold == "yes":
    gold += 5
    print(f"\n\t Hello {miner}, your total number of gold is {gold}")
else:
    print(f"\n\t Hello {miner}, your total number of gold is {gold}")
