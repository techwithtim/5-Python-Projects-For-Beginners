print('Wellcome to my Computer game! ')

playing = input('Do u Want to play!')
if playing != 'yes':
    quit()

print("Ok Let's play : ) ")
score = 0




print('''What Does CPU Stands for?
            a)central processing unit.
            b)graphics processing unit.
            c)random access memory.
            d)power supply
        ''')
answer = input('answer :')       
if answer == 'a':
    print('Correct!')
    score += 1
else:
    print('Incrrect!!!')

print('''What Does GPU Stands for?
            a)central processing unit.
            b)graphics processing unit.
            c)random access memory.
            d)power supply

        ''')
answer = input('answer :')
if answer == 'b':
    print('Correct!')
    score += 1
else:
    print('Incrrect!!!')          

print('''What Does RAM Stands for?
            a)central processing unit.
            b)graphics processing unit.
            c)random access memory.
            d)power supply 
        ''')
answer = input('answer :') 
if answer == 'random access memory':
    print('Correct!')
    score += 1
else:
    print('Incrrect!!!')  

print('''What Does PSU Stands for?
            a)central processing unit.
            b)graphics processing unit.
            c)random access memory.
            d)power supply 
        ''')
answer = input('answer :')
if answer == 'd':
    print('Correct!')
    score += 1
else:
    print('Incrrect!!!')

print('You got' +  str(score) + 'questions correct!')
print('You got' +  str((score/4) * 100)  + '%.')
