name=input("What is your name? ")

print("Welcome", name, "to this adventure.")

answer=input("You are on a dirt road and it has come to and end and you can go right and left. Which way do you wanna go? ").lower()

if answer=="left":
    answer=input("You came across a river. You can walk or swim across it. walk or swim?")
    if answer=="swim":
        print("You swim across and were eaten by a alligator")
    elif answer=="walk":
        print("You walk many miles ran out of water and lost")
    else:
        print("Not a valid option. You lose.")
elif answer=="right":
    answer=input("You came across a bridge but it looks shady will you move back or cross the bridge(cross/back)? ").lower()
    if answer=="back":
        print("You go back and lose")
    elif answer=="cross":
        answer=input("You meet a stranger. Do you talk to them?(yes/no)?").lower()
        if answer=="yes":
            print("You talk to Elon Musk and go to Mars and win the game")
        elif answer=="no":
            print("You lost")
        else:
            print("Not a valid option")
    else:
        print("Not a valid option. You lose")
else:
    print("Not a valid option. You lose")

print("Thank you for playing", name)