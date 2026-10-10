str=input("Enter a string: ")
p=len(str)
str1="AEIOUaeiou"
k=len(str1)
for i in range(0,p):
    for j in range(0,k):
        if str1[j]==str[i]:
            str[i]="$"
print("New string: ",str)