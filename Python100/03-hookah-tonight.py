print('''
**********************************************************************
88                                  88                   88           
88                                  88                   88           
88                                  88                   88           
88,dPPYba,   ,adPPYba,   ,adPPYba,  88   ,d8  ,adPPYYba, 88,dPPYba,   
88P'    "8a a8"     "8a a8"     "8a 88 ,a8"   ""     `Y8 88P'    "8a  
88       88 8b       d8 8b       d8 8888[     ,adPPPPP88 88       88  
88       88 "8a,   ,a8" "8a,   ,a8" 88`"Yba,  88,    ,88 88       88  
88       88  `"YbbdP"'   `"YbbdP"'  88   `Y8a `"8bbdP"Y8 88       88  
***********************************************************************
''')

wannahookah = input("Hookah? Y or N --> ").lower()

if wannahookah == "y":
    place = input("Where? Your place, Pasha at SF, or 40 thieves Santa Clara --> ")
    time = input("What time? ")
    print(f"See you in {place} at {time}!")
    
else:
    print("pidr!")