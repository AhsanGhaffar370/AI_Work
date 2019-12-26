'''

                            Online Python Interpreter.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''


#################################TASK_01#####################
def sum(x,y,z):
    if x in range(13,20):
        x= 0
    if y in range(13,20):
        y= 0
    if z in range(13,20):
        z= 0
    
    return x+y+z
    
a=int(input("Enter value of a:" ))
b=int(input("Enter value of b:" ))
c=int(input("Enter value of c:" ))

print("\nAnswer: "+str(sum(a,b,c)))




#################################TASK_02#####################
def count(string):
    low=0
    upp=0 
    dig=0
    spe=0
    
    for i in string:
        if i.islower():
            low+=1
        elif i.isupper():
            upp+=1
        elif i.isdigit():
            dig+=1
        else:
            spe+=1
    
    return low,upp,dig,spe

string=input("enter String: ")

a,b,c,d=list(count(string))

print("lower:{}  upper:{}  Digit:{}  special:{}".format(str(a),str(b),str(c),str(d)))





#################################TASK_03#####################
str1=input("enter String: ")
c=[]

for i in str1:
    if i.isdigit():
        c.append(int(i))

print("Sum: ",sum(c))
print("Average: ",sum(c)/len(c))





#################################TASK_04#####################
list1=[]

for i in range(5):
    inp=int(input("enter element: "))
    
    list1.append(inp)


print("Minimum",min(list1))
print("Maximum",max(list1))
print("Difference",max(list1)-min(list1))




#################################TASK_05#####################
str1=input("enter String: ")
c=0

for i in range(len(str1)):
    
    if str1[i].lower()=="a" and str1[i+2].lower()=="t":
        c+=1
        
print("count= ",c)



    
