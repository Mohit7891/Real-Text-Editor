# print("this is double \\\\ backslase")
# print("this is /\\/\\/\\/\\ mountain ")
# print("He is \t\t awesome")
# print(r"\" \n \t \'")
# name ="MOHIT"
# print(name[1])
# a=input("Enter your name: ")
# print(a[::])
# import random winning_score = random.randint(0,10)
# guessed_score=int(input("Enter your guessed score: "))
# if winning_score==guessed_score:
#     print("You win!")
# else:
#     if winning_score<guessed_score:
#         print("You guessed too high")
#     if winning_score>guessed_score:
#         print("You guessed too low")
# name,age=input("Please enter name and age:").split(",")
# if name[0]== "a" or name[0]== "A" and age >=10:
#     print("you can watch this game")
# else:
#     print("you can't watch this game")

# n=int(input("Please enter a number"))
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)
# a=input("Enter your name: ")
# i=0
# while i<len(a):
#     print(f"{a[i]}:{a.count(a[i])}")
#     i+=1
# sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)

# number=int(input("Enter your number"))
# winning_number=56
# count=1 
# game_over=False
# while not game_over:
#     if number==winning_number:
#         print("You win")
#         print(f"You guessed {count} times") 
#         break
#     else:
#         if number<winning_number:
#             print("Too low")
#             count+=1
#             number=int(input("Guess again"))
#         else:
#             print("Too high")
#             count+=1
#             number=int(input("Guess again")) 
    
# def gretest(a,b):
#     return b if b>a else a

# print(gretest(2,3))

# def is_palindrome(a):
#     return True if a[::-1]==a[::1] else False

# print(is_palindrome("namn"))
# def reverse(l):
#     new=[]
#     for i in range(len(l)):
#         popped_item=l.pop())
#         new.append(popped_item)
#     return new

# print(reverse([1,2,3]))

# def reverse(l):
#     element=[]
#     for i in l:
#         element.append(l[::-1])
#     return element

# print(reverse(["MOhit","hfg","ghfs"]))
   
# number=input("Enter a number: ")
# sum=0
# for i in range(len(number)):
#     sum+=int(number[i])
#     i+=1

# print(sum)

# name=input("Enter your name: ")
# i=0
# temp_var=[]
# while i<len(name):
#     if name[i] not in temp_var:
#         temp_var.append(name[i])
#         print(f"{name[i]}:{name.count(name[i])}")
#     i+=1

# def type_find(l):
#     count=0
#     for i in l:
#         if type(i) == list:
#             count+= 1
#     return count


# mixed=[1,2,3,[4,5]]
# print(type_find(mixed))

# def cube_finder(n):
#     cubes = {}
#     for i in range(1,n):
#         cubes[i]=i**3
#     return cubes

# print(cube_finder(3))

# user={}
# length=int(input("enter length of data : "))
# key=None
# value=None
# for i in range(1,length+1):
#     key=input("enter key : ")
#     value=input("enter value : ")
#     user[key]=value
# # print(user)
# for keys,values in user.items():
#     print(f"{keys}:{values}",end='\n')

# l=['mohit','mayank','Mukul']
# reverse_list=[ i[::-1] for i in l]
# print(reverse_list)

# def function(num ,*args):
#     return [nums**num for nums in args ]

# cube=[2,3,4]
# print(function(4,*cube))

# def names(l ,**kwargs):
#      for i in kwargs:
#         print(i[o].title())

# name=names("mohit")

# print(name)

# def indexf(l,s):
#     for index2, i in enumerate(l):
#         if i==s:
#             return index2
#     else:
#          -1

# print(indexf(["MOhit","Mukul","MEHUL"],"Mukul"))

# a=lambda *args:list(map(lambda i: sum(i)/len(i),list(zip(*args))))
# print(a([1,2,3],[5,6,7])) 

# from functools import wraps
# def any_data_type(data_type):
#     def decorator_function(function):
#         @wraps(function)
#         def wrapper(*args, **kwargs):
#             if all ([type(arg) == data_type for arg in args]):
#                  return function(*args, **kwargs)
#             print("Invalid data type")
#         return wrapper
#     return decorator_function


# @any_data_type(int)

# def square_finder(*args):
#     return [i**2 for i in args]

# print(square_finder(1,2,3,4))

# def odd_even_finder(n):
#     for i in range(1,n+1):
#         if i%2==0:
#             yield i

# for num in odd_even_finder(6):
#     print(num)
# class laptop:
#     def __init__(self,brand, moddel,price):
#         self.brand = brand
#         self.moddel = moddel
#         self.price = price

#     def apply_discount(self,n):
#         off_price = (n/100)*self.price
#         return self.price-off_price
#         # print(f"Price is {self.discount}")

# l1 = laptop("dj","dh",500)

# print(l1.brand)
# print(l1.apply_discount(50))
# from tkinter import *  
# parent = Tk()  
# redbutton = Button(parent, text = "Red", fg = "red")  
# redbutton.pack( side = LEFT)  
# greenbutton = Button(parent, text = "Black", fg = "black")  
# greenbutton.pack( side = RIGHT )  
# bluebutton = Button(parent, text = "Blue", fg = "blue")  
# bluebutton.pack( side = TOP )  
# blackbutton = Button(parent, text = "Green", fg = "red")  
# blackbutton.pack( side = BOTTOM)  
# parent.mainloop()  

# from tkinter import *   
  
# top = Tk()  
  
# top.geometry("200x100")  
  
# def fun():  
#     messagebox.showinfo("Hello", "Red Button clicked")  
  
  
# b1 = Button(top,text = "Red",command = fun,activeforeground = "red",activebackground = "pink",pady=10)  
  
# b2 = Button(top, text = "Blue",activeforeground = "blue",activebackground = "pink",pady=10)  
  
# b3 = Button(top, text = "Green",activeforeground = "green",activebackground = "pink",pady = 10)  
  
# b4 = Button(top, text = "Yellow",activeforeground = "yellow",activebackground = "pink",pady = 10)  
  
# b1.pack(side = LEFT)  
  
# b2.pack(side = RIGHT)  
  
# b3.pack(side = TOP)  
  
# b4.pack(side = BOTTOM)  
  
# top.mainloop()  

import calendar  
yy = int(input("Enter year: "))  
mm = int(input("Enter month: "))    
print(calendar.month(yy,mm))  