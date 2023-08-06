def print_lol(listh):
    for each_item in listh:
        if isinstance(each_item,list):
            for inside in each_item:
                print(inside)
        else:
            print(each_item)
listh=["The holy Grail","1975","Terry Jones","91",["Graham",["Michael","John","Terry","Eric"]]]
print(print_lol(listh))
print(print_lol(each_item))
