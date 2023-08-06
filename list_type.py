# input=[true,false,[1,2,3],1,1.0,3]
# output= [1,1.0,3]
def recognise_type(l1):
    new_list=[str(i) for i in l1 if(type(i)==int or type(i)==float)  ]
    return print(new_list)
list1=[True,False,[1,2,3],1,1.0,3]
recognise_type(list1)