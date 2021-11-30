# def common_finder(l1,l2):
#     common=[]
#     for i in l1 :
#         if i in l2 :
#             common.append(i)
#     return common

# num1=[1,2,3,4,5,6,7,8,9]
# num2=[1,2,3,4,5]
# print(common_finder(num1,num2))
    
# user_info={}
# user_info["name"]="Mohit"
# print(user_info)
# if "name" in user_info:
#     print("present")

# def cube_finder(n):
#     cubes={}

#     for i in range(1,n+1):
#         cubes[i] =i**3
#     return cubes

# print(cube_finder(5))

# def reverse_list(l):
#     rev=[]
#     for i in l:
#         rev.append(i)
#     return rev

# print(reverse_list(["abv","hgf"]))
# def square_finder(l):
#     return [i**2 for i in l]

# print(square_finder(range(1,11)))
# def all_total(*args):
   
#     return (total for num in args total+=num)

# print(all_total(1,2,3,4))

# print(lambda a,b:a+b)


# def func(num,*args):
#     return [i**num for i in args]

# print(func(2,3,4))



def reverse_string(l,**kwargs):
    l1=[]
    for i in l:
        l1.append(i[::-1].title())
    return l1
l2=["mohit",'jain']
print(reverse_string(l2))




