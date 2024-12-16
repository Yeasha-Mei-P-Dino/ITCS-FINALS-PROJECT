#keep on asking for a name until user types stop, once the loop stopped count the number of names given
count = 0
while True:
	name = input("\n\t Please enter a name: ") 
	if name.lower() == "stop":
		print("\n\t Loop has now stopped") 
		print(f"\n\t You have entered {count} number of names. ") 
		break
	else:
		count += 1 
		continue