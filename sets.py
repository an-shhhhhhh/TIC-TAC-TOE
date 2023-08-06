set={1,2,4,6,4,8,9,3,3,4,5,5,7,9,"f","hhhhhhh"}
print(set)
# set.add("added")
# print(set)
# set.discard("h")
# print(set.clear())
s1=set.copy()
s1.add("anshika")
if set is s1:
    print("preesnt")
else:
    print("np")
for item in set:
    print(item)
print(s1 | set)
print(s1 & set)