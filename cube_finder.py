# function that takes a number n and return a dictionary that contains cube of numbers from 1 to n
def cube_finder(num):
    dict1={}
    for i in range(1,num+1):
        dict1[i]=i**3
    return print(dict1)
cube_finder(10)
