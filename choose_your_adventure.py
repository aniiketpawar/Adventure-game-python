name = input("Type your name: ")
print("Welcom", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way do you want to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around or swim to swim across: ").lower()

    if answer == "swim":
        print("You swam across and were eaten by an aligator.")
    elif answer == "walk":
        print("You walked many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back to the main road. Now you can decide to drive to home. You lose.")
    elif answer == "cross":
        
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no): ")
        if answer == "yes":
            print("You talk to the stanger and they give you the gold and you win!")
        elif answer == "no":
            print("You ignore the stranger and you offended them and you lose.")
        else:
            print("You lose.")
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank you for trying ", name)