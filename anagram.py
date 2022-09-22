str1 = input("Enter the First String  = ")
str2 = input("Enter the Second String = ")

if(sorted(str1) == sorted(str2)):
    print("Two Strings are Anagrams.")
else:
    print("Two Strings are not Anagrams.")