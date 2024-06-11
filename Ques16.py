#Write a program in python that counts the frequency of each character in
#a string.
string=input("enter the string")
n=len(string)
for i in range(0,n):
    count=string.count(string[i])
    print("the freq of ",string[i],"is ",count)