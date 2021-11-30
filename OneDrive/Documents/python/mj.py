# # # # name="Mohit"
# # # # print(name.center(11, "*"))
# # # #
# # # # for i in range(1,10,2):
   
# # # import random
# # # random.randint(1,100)
# # # num=input("enter a number")
# # # total=0
# # # for i in num:
# # #     total+=int(i)

# # # print(total)
# name="MOHIT"
# for i in name:
# # #     print(i)
# # if 'o' in "MOHIT":
# #     print("true")
# # else:
# #     print("not")
# string="MOHIT JAIN"
# print(string)
# print(string.replace(" ","_"))
# string="MY NAME IS MOHIT JAIN"
# print(string.find("IS"))
# print(name.center(15,"*"))
# print(name.replace("O","K"))
# print(name)
fruits1=["mango","apple","greapes"]
name=["kuldeep","Mohit"]
# print(fruits)
# fruits.append("banana")
# print(fruits)
# fruits.insert(2,"banana")
# print(fruits)
# fruits1.extend(fruits2)
# del fruits1[1]
# print(fruits1)
# a=fruits1.pop(2)
# print(fruits1)
# print(a)
# fruits1.remove("greapes")
# print(fruits1)
# if "apple" in fruits1:
#     print("present")
# else:
#     print("npresent")    
# name.sort()
# print(name)
# print(sorted(fruits1))
# fruits1.clear()
# print(fruits1)
# # fruits1.append("apple")
# # print(fruits1)
# a=fruits1.copy()
# print(a)
# user_info="MOHIT,5".split("    ,    ")
# print(user_info)
# print(",".join(user_info))
# for fruit in fruits1:
#     print(fruit)

# i=0
# while i<len(fruits1):
#     print(fruits1[i])
#     i+=1
# matrix=[[1,2,3],[4,5,6]]
# for i in matrix:
#     for j in i:
#         print(j)
    
# print(type(matrix))  
# num=list(range(1,11,2))
# print(num)
# print(num.index(3))
# mixed=(1,2,3,4,5)
# for i in  mixed:
#     print(i)

# print(type(mixed))
# nums=1,
# print(type(nums))    
# guitaristss=("Manoj","Mohit","Jay")
# # guitarists1,guitarists2,guitarists3=(guitaristss)
# print(guitaristss) 

# fav=("MOHIT","SHUBHANSHU",["JAY","HARDIK"])
# fav[2].pop()
# print(fav)
# fav[2].append("we made it")
# print(fav)
# user={"name":"mohit","age":24}   
# user=dict(name="mohit",age=24)
# print(user)
# print(user["name"])
# user_info={}
# user_info["name"]="Mohit"
# print(user_info)
# user_info={
#     "name":"mohit","age":20}
# if "name" in user_info:
#     print("present")

# if 20 in user_info.values():
#     print("present")

# for i in user_info:
#     print(i)
    
# print(user_info.values())


# # items method
# user_items=user_info.items()
# print(user_items)
# print(type(user_items))

# for i,j in user_items:
#     print(f"key is {i} and value is {j}")
# user_info["fav songs"]=["song1","song2"]
# print(user_info)

# more_info={"fav songs":"rajsthan"}
# user_info.update(more_info)
# print(user_info)
# d=dict.fromkeys("abc","unknown",)
# print(d)
# d={"name":"Mohit","age":"unknown"}
# print(d.get("name"))
#set union & intersection
# s1={1,2,3,4}
# s2={3,4,5,6}
# union_set=s1|s2 #unin
# print(union_set)
# print(s1 & s2)
# negative=[]
# for i in range(1,11):
#     negative.append(-i)
# print(negative)

# new_negative=[-i for i in range(1,11)]
# print(new_negative)        #short trick
# square={num:num**2 for num in range(1,5)}
# print(square)

# def total(a,b):
#     return a+b
# def all_total(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total
# print(all_total(1,2,3,4,5))
# print(total(2,3)) 
# def func(**kwargs):
#     print(kwargs)
# func(first_name="MOHIT",last_name="JAIN")       
# add2=lambda a,b: a+b
# print(add2(5,3))
# names=["MOHIT","JAY","SHUBHANSHU"]
# for pos,name in enumerate(names):
#     print(f"{pos}------>{name}")

# numbers=[1,3,4,5]    #map method
# def square(a):
#     return a**2
# squares=list(map(square,numbers))
# print(squares)

# def is_even(a):  #filter numbers
#     return a%2==0
# numbers=[3,4,5,7,8,5,34,56]
# evens=tuple(filter(is_even,numbers))
# print(evens)

# user_id=["use1","user2","user3"]
# names=["MOHIT","JAY","SHUBHANSHU"]
# print(list(zip(user_id,names)))
def decorator_function(any_function):
    def wrapper_function():
        print("this is awesome function")
        any_function()
    return wrapper_function    


def any_function():
    print("this is function 1")

func2=decorator_function(any_function)
func2()
