def anagram_fuggveny(str1, str2):
    if(sorted(str1) == sorted(str2)):
        return "Two Strings are Anagrams."
    else:
        return "Two Strings are not Anagrams."

str1 = input("Enter the First String  = ")
str2 = input("Enter the Second String = ")
result = anagram_fuggveny(str1, str2)
print(anagram_fuggveny(str1, str2))