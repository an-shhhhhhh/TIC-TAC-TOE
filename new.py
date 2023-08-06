# #code to add two numbers
# num1=10
# num2=4
# sum=num1+num2
# print(f"The sum of two numbers {num1} and {num2} is {sum}")
#




# #code to add two numbers privided by user
# num1=int(input("Enter the value of first number"))
# num2=int(input("Enter the value of second number"))
# sum=num1+num2
# print(f"The sum of two numbers {num1} and {num2} is {sum}")
#




# #program to find factorial of a number
# def factorial(num):
#     if(num<0):
#         fact=0
#     elif(num==0 or num==1):
#         fact=1
#     else:
#         answer=1
#         for i in range(1,num+1):
#             answer=answer*i
#         fact=answer
#     return print(f"The factorial of {num} is equal to {fact}");
# number=int(input("Enter the number whose variable you want to find:"))
# factorial(number)





#program to find simple interest:
# def SI(principle,rate,time):
#     Simple_Interest=(principle*rate*time)/100
#     return print(f"The Simple Interest for the given values of Principle, Rate and Time is {Simple_Interest}.")
# P=int(input("Enter the value of principle: "))
# R=int(input("Enter the value of rate: "))
# T=int(input("Enter the value of time: "))
# SI(P,R,T)




#program to find compound interest:
# def CI(principle,rate,time):
#     amount=principle*pow((1+rate/100),time)
#     compound_interest=amount-principle
#     return print(f"Compound Interest for the values of principle:{principle} ,rate:{rate} and time:{time} is {compound_interest}")
# P=int(input("Enter the value of principle: "))
# R=float(input("Enter the value of rate: "))
# T=int(input("Enter the value of time: "))
# CI(P,R,T)
# # 10000, 10.25, 5




# program to find whether the given number is perfect or not
# example:
# Input: n = 15
# Output: false
# Divisors of 15 are 1, 3 and 5. Sum of
# divisors is 9 which is not equal to 15.
#
# Input: n = 6
# Output: true
# Divisors of 6 are 1, 2 and 3. Sum of
# divisors is 6.
# abc = [0]

# def ifPerfect(num):
#     for i in range(1,num):
#         if(num%i==0):
#             abc.append(i)
#     for i in abc:
#         sum=0
#         sum=sum+i
#     if sum==num:
#         return print(f"{num} is a perfect square.")
#     else:
#         return print(f"{num} is not a perfect number.")
# number=int(input("Enter the number to check:"))
# ifPerfect(number)



# # program to print all the prime numbers from 1-N
# def ifPrime(n):
#     for i in range(2,n):
#         if i%2==0:
#             continue
#         elif i%(i-1)==0:
#             # print("This number is not a prime number.")
#             continue
#         else:
#             print(i)
# number=int(input("Enter the range upto which you want to see the prime numbers:"))
# ifPrime(number)





# program to print all the prime numbers in a given range:
# def ifPrime(a,b):
#     for i in range(a,b):
#         if i==2:
#             print(i)
#         elif i%2==0:
#             continue
#         else:
#             if i == 0:
#                 continue
#             else:
#                 if i%(i-1)==0:
#                     # print("This number is not a prime number.")
#                     continue
#                 else:
#                     print(i)
# starting_range=int(input("Enter the starting range"))
# ending_range=int(input("Enter the ending range"))
# ifPrime(starting_range,ending_range)





# program to check whether a number is prime or not
# def isPrime(num):
#     for i in range(1, num):
#         # if i % 2 == 0:
#         #     return print("False")
#         # for n in range(1,i):
#         #  i%(i-1)==0:
#         if num%i==0:
#             return print("False")
#         else:
#             return print("True")
# number=int(input("Enter the number to be checked whether it is prime or not:"))
# isPrime(number)



# program to check whether the giveen number is a fibonacci number or not
# we have a formula to find the following :
# A number is Fibonacci if and only if one or both of (5*n^2 + 4) or (5*n^2 – 4) is a perfect square
# def isFibonacci(n):
#     num1=int(pow(((5*pow(n,2))+4),1/2))
#     num2=int(pow(((5*pow(n,2))-4),1/2))
#     if (((num1*num1==5*pow(n,2))+4) or (num2*num2==5*pow(n,2)-4)):
#     # if(num1==int or num2==int):
#         print("The given number is a fibonacci number. ")
#     else:
#         print("The given number is not a fibonacci number. ")
# number=int(input("Enter the number to be checked as fibonacci or not:"))
# isFibonacci(number)




# program to find the ascii value of variables.
# def ascii_value(var):
#     return print(f"The ASCII value of {var} is {ord(var)}")
# variable=input("Enter the variable whose ascii value you want to find:")
# ascii_value(variable)



# # program to find the square of numbers upto n:1^2+2^2+3^2.....n^2
# def sum_squares_numbers(n):
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+i*i
#     return print(sum)
# var=int(input("Enter the range upto which you want to find the square of numbers:"))
# sum_squares_numbers(var)





# program to find the cube of numbers upto n:1^2+2^2+3^2.....n^2
# def sum_cubes_numbers(n):
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+i*i*i
#     return print(sum)
# var=int(input("Enter the range upto which you want to find the cube of numbers:"))
# sum_cubes_numbers(var)






# program to find the sum of elements of an array
# def summation(arr):
#     sum=0
#     arr=[15,12,13,10]
#     for i in arr:
#         sum=sum+i
#     print(sum)







# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
# Array:[1,2,3,4,5,6,7]
# Rotation of the above array by 2 will make array
# ArrayRotation1:[3,4,5,6,7,1,2]
def arrayRotation(arr,d):
    for i in range(0,d):
        temp = arr[0]
        for j in range(0,len(arr)-1):
            arr[j]=arr[j+1]
            arr[len(arr)-1]=temp
    for i in range(0,len(arr)):
        print(arr[i])
a=int(input(("Enter no. of elements")))
print("Enter",a,"integer elements")
array1=[]
for i in range(a):
   array1.append(int(input()))
print("Array entered by user is",array1)
dd=input("Enter the element from which you want to rotate")
arrayRotation(array1,dd,a)













