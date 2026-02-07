a = [1,2,9,3,4,5]
b = ["apple","Banana","grapes","apple"]
c = list(("apple","Banana"))
# print(a)
# print(b)
# print(c)
# print(len(b))   

# print(b[1])
# print(b[2:3])
# print(b[::-1])

# if "apple" in b:
#     print("Yes")

# b[3] = "orange"
# print(b)

# b[2:4] = "grapes","banana","mango"
# print(b)

# b.append("orange")
# print(b)

# b.insert(1,"orange")
# print(b)

# a.extend(b)
# print(a)


# b.remove("apple")
# print(b)

# b.pop(2)
# print(b)  #deletse specified Index

# b.pop()   removes last element without speciefy the Index 
# print(b)

# del a[2]
# print(a)

# del a       deletes the entire list
# print(a)

# a.clear()       it clears the all values but keeps set alive 
# print(a)


# for i in b:
#     print(i)

# for i in range(len(b)):
#     print(b[i])

# i=0
# while i < len(b):
#     print(b[i])
#     i += 1

# [print(x) for x in b]

# print({n for n in a})
# print([n for n in a])


# for i in b:
#     if "B" == i[0] or "b" == i[0]:
#         print(i)

# empy = []
# for i in b:
#     if "a" == i[0]:
#         empy.append(i)
# print(empy)

# empy = [i for i in b if "a" == i[0]]
# print(empy)


# empy  = [i for i in b]
# print(empy)


# b.sort()
# print(b)
# a.sort()
# print(a)

# a.sort(reverse = True)
# print(a)

# def Func(n):
#     return abs(n-4)

# a.sort(key=Func)
# print(a)

# b.sort(key =str.lower)
# print(b)

# print(b.reverse())

# d = a.copy()
# print(d)   copying the list using copy keyword

# d = list(a)   copying the list using list keyword 
# print(d)

# d = a[:]        copyes the list with using  : 
# print(d)

# print(a+b)

# for i in b:
#     a.append(i)
# print(a)

# a.append(b)
# print(a)