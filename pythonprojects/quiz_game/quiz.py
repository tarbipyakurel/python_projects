print("Welcome to my game")

reply=input("Do you want to continue to the game? ")

score=0

if reply.lower()!="yes":
    quit()

print("Let's play :)")


answer=input("What is the full form of CPU? ")

if answer.lower()=="central processing unit":
    print("correct")
    score+=1
else:
    print("incorrect")

answer=input("What is the full form of RAM? ")

if answer.lower()=="random access memory":
    print("correct")
    score+=1
else:
    print("incorrect")

answer=input("What is the full form of ML? ")

if answer.lower()=="machine learning":
    print("correct")
    score+=1
else:
    print("incorrect")

answer=input("What is the full form of ROM? ")

if answer.lower()=="read only memory":
    print("correct")
    score+=1
else:
    print("incorrect")

answer=input("What is the full form of WWW? ")

if answer.lower()=="world wide web":

    print("correct")
    score+=1
else:
    print("incorrect")

print("You got " + str((score/5)*100) + "%.")
print("Your total score is "+str(score))

if score==5:
    print("You won 10 bucks")
else:
    print("Answer all 5 questions correctly to win 10 bucks")


