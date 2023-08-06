# This is a program to print a scenery
# code for mountain
for i in range(0,10):
    for j in range(0,45):
        print(end=" ")
    for j in range(0,i+1):
        print(" ", end="\n")
    print("")

# code for horizon
i=0
while i<=180:
    print("_",end="")
    i=i+1
