#["abc","tuv","xyz"]=["cba,"vut","zyx"]
list1=["abc",'tuv','xyz']
k=[]
for i in list1:
    k.append(i[::-1])
print(k)
#
# def reverse_elements(l):
#     elements=[]
#     for i in l