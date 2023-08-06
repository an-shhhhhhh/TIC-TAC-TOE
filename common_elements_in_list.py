# input=[1,2,5,8],[1,2,7,6]
# output=[1,2]
def common_elements(list1,list2):
    list3=[]
    for i in list1:
        if i in list2:
            list3.append(i)
    return print(list3)
elements1=[1,2,5,8]
elements2=[1,2,7,6]
common_elements(elements1,elements2)