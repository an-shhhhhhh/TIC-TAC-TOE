# this is based upon printing an emoji
# go to the website unicode.org ,their we can see the code of all the emojis we need to copy them and
print("\U0001F618")
# insert backslash inm front of it
# and replace + with 000
rows=6
for i in range(1,rows+1):
    for j in range(1,i-1):
        print(j, end=" ")
    for j in range(i-1,0,-1):
        print(j, end=" ")
    print()