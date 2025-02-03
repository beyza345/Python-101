""" #nameFunctions
def hello(name):
    print('Hello ' + name)

hello('Alice')
hello('Bob')
#randomFunctions
import random
def getAnswer(answerNo):
 if answerNo==1:
   return 'its certain'
 elif answerNo==2:
   return 'maybe'
 elif answerNo==3:
   return 'fortunately'
 elif answerNo==4:
   return 'luckly'
 elif answerNo==5:
   return 'no'
r=random.randint(1,6)
print(getAnswer(r)) """
#StacksFavourite
""" def a():
       print('a() starts')
       b()
       d()
       print('a() returns')

   
def b():
       print('b() starts')
       c()
       print('b() returns')

def c():
       print('c() starts')
       print('c() returns')

def d():
       print('d() starts')
       print('d() returns')
a()
 """
#arraysOnTheLists
""" spam["rat","bird","sheep","cow"]
for i in range(0,4):
    print(array[i])
    i+=i """
#sumOfArray
def sum(array):
    sum=0
    for i in array:
        sum+=i
    return sum
list=[1,2,3,4,5]
print(sum(list))
#summary
def sum(array):
    sum=0
    for i in array:
        sum+=i
    return sum
array=[7,6,8,4,7]
print(sum(array))
#myCats
""" catNames=[]
while True:
    print("enter your cat name"+"(or enter nothing to stop)")
    name=input()
    if name=='':
        break
    catNames=catNames+[name]
print('cat names are:')
for name in catNames:
    print(''+name)    
   """
#isItBelongs
myPets=['sophie','sulo','fatty']
print("enter a pet name")
name=input()
if name not in myPets:
    print('I do not belong'+ name)
else:
    print(name+ "is my pet")    




      