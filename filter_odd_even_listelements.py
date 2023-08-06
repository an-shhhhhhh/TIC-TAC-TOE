# [1,2,3,4,5,6,7]=[[1,3,5,7],[2,4,6]]
def filter_odd_even(list1):
    list2=[]
    list3=[]
    list4=[]
    for i in list1:
        if i%2==0:
            list2.append(i)
        else:
            list3.append(i)
    return print([list3]+[list2])
elements=[1,2,3,4,5,6,7]
filter_odd_even(elements)


