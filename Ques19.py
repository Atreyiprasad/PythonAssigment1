#Write a python program that removes all punctuation from a given string.
string=input("enter the string:")
n=len(string)
ans=""
for i in range(0,n):
    if(string[i]>='a' and string[i]>='z'):
        ans=ans+string[i]

print("the string is: ",ans)
