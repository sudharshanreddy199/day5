#---->common function for list
'''
l1=[6,7,8,9,0]
print(len(l1))
print(max(l1))
print(min(l1))
'''
'''
l1=[6,7,8,9,"p","u"]
print(max(l1))
print(min(l1))
'''
'''
l1=[6,7,8,9,0,8.89,-5,0.78]
print(min(l1))
'''
'''
l1=[6,7,8,9,0,8.9,-5,0.78]
index()
print(l1.index(9))
'''
'''
l1=[6,7,8,9,0,8.9,-5,0.78]
count()
print(l1.count(6))
'''

# some funtions which is specifically used for list

#to add element inside list
#insert() -->to add element at specific index position
'''
l1=[6,7,8,9,0,8.9,-5,0.78]
l1.insert(2,"cars")
print(l1)
# --> to delete element from list
l1=[6,7,8,9,0,8.9,-5,0.78]
pop()
l1.pop()
print(l1)
'''
'''
# pop (index_value)-->used to delete element at specific index
l1.pop(4)
print(l1)
'''

# remove(element)---> used to delete element directly
'''
l1.remove(8.89)
print(l1)
'''
# clear()--> to complete delete all element in list
'''
l1.clear()
print(l1)
'''

#del--> to delete the list
'''
del l1
print(l1)
'''

#---> join 2 list
'''
l1=[9,0,8]
l2=["p","o","t",34]
print(l1+l2)
'''

#extend()--> to combine 2 lists
'''
l1.extend(12)
print(l1)
'''
#---> copy()
'''
l1=[6,7,8,9,3]
l2=l1.copy()
print(l2)
print(l1)
print(id(l1))
print(id(l2))
'''
#---> diff between shallow copy and deep copy
# shallow copy
#imort copy
'''
l1=[8,9,0,[5,6],[3,2,1]]
l2=copy.copy(l1)
l1.append(890)
print(l1)
print(l2)
'''
# deep copy --> used to copy the list with nested list
# import copy
'''
l1=[8,9,0,[5,6],[3,2,1]]
print(l1[]-1[1])
l2=copy.deepcopy(l1)
l1[-1].append('cars')
print(l1)
print(l2)
'''
# sort--> arrange element in list in ascending or discending order
'''
l1=[9,7,45,0,-6,5,12]
l1.sort()
print(l1)
l1.sort(reverse=true)
print(l1)
l1=['z','i','o','p','9']
l1.sort()
print(l1)
'''
# list constructor
# list()---. to conver other collection datatype to list
'''
l3=((8,9,0))
print(list(l3))
l4=(8,90
print(list(l4)
'''

# ---> nested list
'''
l1=[8,9,[0,8,7],ArithmeticError["p","o",'y'],[8,'t']]
p[rint(l1[-2][1])
print(l1[1:4])
print(l1[1:-1])
'''
# to delete "t" from l1
'''
l1[-1].remove('t')
print(l1)
'''
# combine these 



# ! ----> Tuple

1.) tuple have to be surrounded by ()
2.) The element inside tuple are not changable
3.) The element inside tuple are indexed
4.) The element will excuted in order
5.) It is heterogenous
6.) It allow duplicate element
l1=[8]
'''
print(type(l1))#list

l1=(8,)
print(type(l1))#tuple

l1=8,9
print(type(l1))#tuple
'''
#len(),min(),max(),index(),count()--->all same as list
# to add  element inside tuple ---> cannot add
# cannot delete any element from tuple


# * jon 2 tuples
'''
t1 = (8, 9, 0)
t2 = (6, 7, 8)
print(t1 + t2)

# To add all element inside list and tuple
sum()
l1 = (8, 9, 7, 6)
prin
LE-348 S.Nagoor basha
11:40 AM
oldman got covid,,,in csk camp
'''
# To add all element inside list and tuple
#sum()
#l1 = (8, 9, 7, 6)
#print(sum(l1))



# * sort tuple
#t1 = (8, 9,0, 89, 12)
#print(tuple(sorted(t1)))
#print(tuple(sorted(t1, reverse=True)))

# * Iterate list and tuples
'''
l1 = [9, 8, 0, 6, 5]
for i in l1:
    print(i)
'''
# Iterate based on index value
'''
l1=[9,8,0,6,5,7,36,54,55,6,43,5,66]
for i in range(0,len(l1)):
    print(l1[i])
'''
































































