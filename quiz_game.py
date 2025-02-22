print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").lower()

if playing == "yes":
    print("Okay! Let's play :)")
score = 0

if playing == "no":
    print("Oh, sorry to see you go so soon, :( ")
    quit()

print("Please answer yes or no, in the upcoming question")

q1 = input("What does CPU stand for? ").lower()
if q1 == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

q2 = input("What does GPU stand for? ").lower()
if q2 == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

q3 = input("What does RAM stand for? ").lower()
if q3 == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

q4 = input("What does PSU stand for? ").lower()
if q4 == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
print("Thanks For Playing The Computer Quiz!")
