'''

                            Online Python Interpreter.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''


# ##############  TASK01  ##############
# def ret(n):
#   temp=n.split()
#   print(temp[::-1])

# s1=input("Enter a sentence:")
# ret(s1)




# # ##############  TASK02  ##############
# def pangram(str1):
#   alph = "abcdefghijklmnopqrstuvwxyz"
#   for i in alph: 
#     if i not in str1.lower(): 
#       return False
#   return True

# s2=input("Enter a sentence:")

# if(pangram(s2)): 
#   print("String is Pangram") 
# else: 
#   print("String is not Pangram") 




# # ##############  TASK03  ##############
# def hyph(str1):
#   str1=str1.split("-")
#   str1.sort()

#   t=""
#   for i in str1:
#     t+=i+"-"

#   t2=t[0:-1]

#   return t2

# s3=input("Enter Hyphen seperated words:")
# print(hyph(s3))




# # ##############  TASK04  ##############
# def leap(year1):

#   if year1%4==0:
#     if year1%100==0:
#       if year1%400==0:
#         return "leap year"
#       else:
#         return "not leap year"
#     else:
#       return "not leap year"
#   else:
#     return "not leap year"

# year=int(input("Enter any year:"))

# print("The year is",leap(year))


# # # ##############  TASK05  ##############
# def rec(num):

#   if num==1:
#       return 1
#   if num==0:
#     return 0
#   if num>=2:
#     return rec(num-1)+rec(num-2)


# num=int(input("Enter any number:"))
# print("answer of recursion:",rec(num))




# # # ##############  TASK06  ##############
def bunnies(n):
  if (n == 0):
    return 0
  
  if (n % 2 == 1):
    return 2 + bunnies(n-1)
  
  return 3 + bunnies(n-1)


num=int(input("Enter the number of bunnies"))

print("The number of ears are:",bunnies(num))
