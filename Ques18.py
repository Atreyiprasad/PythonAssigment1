#Write a python program that checks if two strings are anagrams of each
#other.

def anagram(word1,word2):
    word1=word1.replace(" ","").lower()
    word2=word2.replace(" ","").lower()

    return sorted(word1)==sorted(word2)

#main function
word1=input("enter the string 1: ")
word2=input("enter the string 2: ")

if anagram(word1,word2):
    print("they are anagram")
else:
    print("not anagram")