name = input("What's your name? ").strip().title()
print(name)

if name =="Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherine")
else:
    print("Who?")


match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherine")
    case _:
        print("Who?")