print("beyza")
#evenOrOdd
num=int(input("pls enter a number"))
if num%2==0:
    print("its even ")
else:
    print("its odd number")   
#writeAllNumbers
num=int(input("enter a number"))
for num in range(0,num,3):
    print(num)
#calculateFactoriel
num=int(input("enter your number"))
factoriel=1
for num in range(1,num+1):
    factoriel=factoriel*num
print(factoriel) 
#pyramidOfStars
num=int(input("enter a numbber"))
for i in range(1,num):
    print("*"*i)