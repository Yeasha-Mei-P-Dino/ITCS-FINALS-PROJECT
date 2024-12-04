#Print hi, name until the user types 'stop'
go = True
while go:
    name = input("\n\t Type any name: ")
    if name.lower() == "stop":
        print("\n\t LOOP TERMINATED \n", "="*120)
        break
        go = False
    else:
        print(f"\n\t Hi {name} ^w^.")
        continue
        
