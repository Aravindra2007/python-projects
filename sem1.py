# import cmath

# l = [10,20,30,10,40,50]
# sum = 0
# for i in l:
#     sum +=i
# print(sum) 

# l.sort()
# print(l)
# print(l[-1])


# lnp = input().split()
# l = [int(item) for item in lnp]
# l1 = []
# for i in l:
#     if i in l1:
#         continue
#     else:
#         l1.append(i)
# print(l1)

# lnp = [10,10,20,20,30,23,20]
# l = set(lnp)
# lp = list(l)
# print(lp)


# l = [1,2,2,1,1,3,3,1,1,21,1]
# count = 0
# num = 1 
# for i in l:
#     if i == 1:
#         count += 1
# print(count)
# print(l.count(num))


# mydict = {}
# name = "sachin"
# age = 18
# city = "kurnool"
# mydict["name"] = name
# mydict["age"] = age
# mydict["city"] = city
# print(mydict)

# mydict = {1:2,2:3,3:4}
# for i,j in mydict.items():
#     print(i,j)


# a = -10
# print(a<<2)
# print(a>>2)
# print(~a)

# b = input(" enter ").split()
# a = [int(item) for item in b]
# print(a)


# n = 5
# for i in range(5,1,-1):
#     print(i)

# i = 0
# while i <= 5:
#     print(i)
#     i+=1

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# n = 5
# for i in range(0,n):
#     for j in range(n):
#         if j < n-i:
#             print(" ",end=" ")
#         else:
#             print("*",end=" ")
#     print()


# for i in range(5):
#     for j in range(5):
#         if 5-j >= i+1:
#             print(" ",end=" ")
#         else:
#             print("*",end=" ")
#     print()



# for i in range(5):
#     for j in range(i,5):
#         print(" ",end=" ")


#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")

#     print()

# str = 'Python is Easy !!!'
# print(str)
# print(str[0])
# print(str[-1])
# print(str[15:17])
# print(str * 2)
# print(str + 'Isn’t it?')

# def fact(n):
#     result  = 1
#     while n > 0:
#         result *= n
#         n -= 1
#     return result

# print(fact(5))


# def fact(n):
#     i = 1
#     while i <= n:
#         if n%i == 0:
#             print(i)
#             i+=1

#         return i

# print(fact(10))


# a = 2
# b = 2
# c = 2
# disc = (b**2)-4*a*c
# print(disc)
# root1 = (-b+disc**2*a)//2*a
# root2 = (-b-disc**2)//2*a
# print(root1,root2)
# if disc > 0:
#     print(" roots are real ")
# else:
#     print(" imagery ")


# for i in range(0,20):
#     n = i*(i+1)
#     i+=1
#     print(n)


# male = input()
# female = input()
# m1 = set(male)
# f1 = set(female)
# allage = f1.union(f1)
# print(allage)

# l = ["hello","world"]
# print(l[0][0])

# l = [10,20,30,40,50,[20,30,40,50]]
# print(l[5][3])

# l = ["10","20"]
# l1 = [int(item) for item in l]
# print(l1)


# l = [10,20,30,40,50]
# l1 = [10,20,30,40,60]
# print(l.extend(l1))
# print(l)

# l = [10,20,30,40,10,50]
# print(len(l))

# def allchar(a):
#     for char in a:
#         return char

# print(allchar("hello"))

# def facto(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)
    
# print(facto(5))


# def func1(n):
#     if n <= 1:
#         return n
    

# def func2(n):
#     if func1(n) == 0:
#         return 0
#     else:
#         return 1
    

# print(func2(0))

# def isprime(n):
#     count = 0
#     for i in range(1,n+1):
#         if n %i == 0:
#             count +=1 
#             if count ==2:
#                 print("prime")

# isprime(7)

# def vowels(a):
#     vowels = "aeiouAEIOU"
#     if a in vowels:
#         return True
    
# # print(vowels("c"))
# import random
# def guasingnumber():
#     n = random.randint(1,100)
#     guess  = None

#     while guess != n:
#         guess = int(input(" enter a number "))
#         if guess < n:
#             print(" guesss is too low")
#         elif guess > n:
#             print(" guess is too high ")
#         else:
#             print(" congratulations you guesswd it ")

# print(guasingnumber())

# def gcd(x,y):
#     if y > x:
#         x,y = y,x
#     rem = x%y
#     if rem == 0:
#         return y
#     else:
#       return gcd(y,rem)
    
# print(gcd(10,5))

# def palin(n):
#     if len(n) < 0:
#         return True
#     else:
#         return n == n[::-1]
    
# n = int(input(" enter a num "))
# s = str(n)
# print(palin(s))


# import num 
# a,b = 10,20
# value = num.add(a,b)
# print(value)

# import calendar
# print(calendar.month(2006,9))

# def print_var(n):
#     print(n)

# n = 10
# print_var(n)
# print(dir())

# l = [1,2,3,4]
# list = list(map(lambda x:x**2 ,l))
# list1 = [int(digit**2) for digit in l]
# print(list1)


# def unique(l):
#     l1 = []
#     for i in l:
#         l1.append(i)
#         l2 = sorted(l1)
#     return l2


# l = [12,32,12,32,2,1]
# print(unique(l))


# name = "aravind"
# age = 18
# print(" my name is %s and my age is %d"%(name,age))

# print(ord('$'))


# z = 3+4j
# print(z.imag)
# print(z.real)


# import os 
# a = open("num.py","r")
# print(a.read())
# a = open("num.py","a")
#     a.write("hello world")
# a.close()
# a = open("num.py","r")
# print(a.read())

# import os 
# a = open("add.py","r")
# print(a.read())
# a = open("add.py","w")
# a.write("jaiballya")
# a.close()
# a= open("add.py","r")
# print(a.read())


# import os 
# a = open("add.py","r")
# print(a.read())
# a = open("add.py","w")
# a.write("jaiballyya")
# a.close()
# a= open("add.py","r")
# print(a.read())


# file = open("add.py","w")
# lines = ["helo world","jai balayya ","supe"]
# file.writelines(lines)
# file.close()
# file = open("add.py",'r")
# print(file.read())


# import os 
# a = os.rename("add.py","ad.py")
# print(a)





# def detail(name,age):
#     print("name: ",name)
#     print("age: ",age)

# detail(name="Aravind",age=18)


# import math
# a = 2
# b = 2
# c = 2
# delta = b**2-4*a*c
# root1 = -(b+cmath.sqrt(delta))//2
# root2 = -(b-cmath.sqrt(delta))//2
# print(root1,root2)




# def function(n):
#     H = 0
#     for i in range(1,n+1):
#         H += (1/i)
#         print(H,end="+")
#     print()


# function(5)

# a = 12
# b =23.5
# c = a+b
# d = a-b
# e = a*b
# f = a/b
# print(" explicity value ")
# print(c)
# print(d)
# print(e)
# print(f)

# print("implicity value ")
# print(int(c))
# print(int(d))
# print(int(e))
# print(int(f))


# a = int(input("enter a number "))
# b = int(input("enter a number "))
# mode  = input(" selct the operand mode ")
# if mode == "and":
#     result = a&b
# elif mode == "or":
#     result = a|b
# elif mode == "xor":
#     result = a^b