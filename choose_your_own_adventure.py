name = input("Type your name: ") #program asks user for name
print("Welcome", name, "to this adventure!") #prints greeting

answer1 = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower() #introduces scenario to user

if answer1 == "left": #if response is 'left'
    answer2 = input( #additional prompt to user
        "You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim across: ").lower()
    #conditionals to answer3
    if answer2 == "swim":
        print("You swam acrross and were eaten by an alligator.")
    elif answer2 == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose.')

elif answer1 == "right": #if response is 'right'
    answer3 = input( #additional prompt
        "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()
    #conditionals
    if answer3 == "back":
        print("You go back and lose.")
    elif answer3 == "cross":
        answer4 = input(
            "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()
        #conditionals
        if answer4 == "yes":
            print("You talk to the stanger and they give you gold. You WIN!")
        elif answer4 == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)#print ending statement
