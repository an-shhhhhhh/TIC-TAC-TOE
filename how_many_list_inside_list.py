# input--> [1,2,3,[1,2],[2,4]]
# output-->2 since 2 list is present in the main list
def count_list(l):
    total=0
    for i in l:
        if type(i)==list:
            total=total+1
    print(total)
    return total

l1=[1,2,3,[1,2],[2,4],[3,4],[6,8],[8]]
count_list(l1)