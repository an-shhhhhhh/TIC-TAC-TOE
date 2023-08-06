# nums=[1,2,3]
# to power(3,*nums)
#
# output=
# list--->[1,8,27]
def args(num,*nums):
    # final_list=[i**num for i in nums]
    return print([i**num for i in nums])
args(2,1,2,3,4,5)
    