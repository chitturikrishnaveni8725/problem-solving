# ASSIGNMENT



# Date : 20-04-2026 
# Tech stack :Python
# Topic: : problem solving
# Dead line :  2days 
# _______________________________________________________
# Task : 
# Problem solving Questions: 

# 1. Write a python program to remove the duplicate in given list.
#                 a = [2,3,4,2,3,4,5,7]
#                 output: [2,3,4,5,7]


a=[2,6,7,2,6,7,10,20]
res=[]
for i in a:
    if i not in res:
        res.append(i)
print(res)   
# 2. Write a program that takes array of numbers as input, among the numbers in array, print the numbers which forms a prime number by adding one to it. Print such numbers in the given array separated b spaces.

#               Testcase1	:  [ 7, 4, 7, 23, 10, 6]
#                Output     	:  4 10 6

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

arr = [7, 4, 7, 23, 10, 6]
result = []
for num in arr:
    if is_prime(num + 1):
        result.append(num)
print(*result)
# 3. Write python program
#  a = " aaabbaaccdd"
# output: "a5b2c2d2”
a="aaabbaaccdd"
res=""
for i in a:
    if i not in res:
        res+=i+str(a.count(i))
print((res))       
a="aabbccdd"
dict={}
for i in a:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
res=""
for i in dict:
    res+=i+str(dict[i])      
print(res)    




