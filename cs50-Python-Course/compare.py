x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print(f"{x} is less than {y}")
elif x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{x} is equal to {y}")


if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")


if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
