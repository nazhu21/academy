
print("Let's play a game.")
print("It's simple, you just have to answer some questions.\n") 

choice1 = input('Do you agree that we should hangout sometime? Type "Yes" or "No" ').lower()

if choice1 == "yes":
    choice2 = input('Great, next question: Are you free this weekend? Type "Yes" or "No" ').lower()
    if choice2 == "yes":

        choice3 = input('Good job, you doing great! Next question then: a)Amusement park or b)Evening Hike? Type "A" or "B" ').lower()
        if choice3 == "a":
            print("Great, it's a date then! This Saturday, I will pick you up at 2pm and we are going to an Amusement Park!")
        else:
            print("Nice! Let's go for a hike! If you have a place in mind, let me know. If not, it's okay, I have a place in mind. This Saturday, I will pick you up at 5pm!")

    else:
        choice2a = input('Next weekend? Type "Yes" or "No" ').lower()
        if choice2a == "yes":
            choice3a = input('Good! Next question then: a)Amusement park or b)Evening Hike? Type "A" or "B" ').lower()
            if choice3a == "a":
                print("Great, it's a date then! Next Saturday, I will pick you up at 2pm and we are going to an Amusement Park!")
            else:
                print("Nice! Let's go for a hike! If you have a place in mind, let me know. If not, it's okay, I have a place in mind. This Saturday, I will pick you up at 5pm!")
        else:
            available = input("When are you available, busy girl? :)")

else:
    print("Okay, nevermind!")



