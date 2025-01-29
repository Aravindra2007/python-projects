## factorial
# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print(fact) 


## maximum of numbers
# def findmax(num1,num2,num3):
#     return max(num1,num2,num3)

# num1 = 123231348
# num2 = 232543123
# num3 = 1212314323
# maximum = findmax(num1,num2,num3)
# print(maximum)

## 
# a = 76
# b = 17
# if a-b >= 17:
#     print(" the number is doubled ",2*(a-b))
# else:
#     print(" single value ",(a-b))


# for i in range(2000,3200):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i,end="' '")

# user = input(" enter something ")

# if user.isdigit():
#     print(" given data is integer:  integer ")
# elif user.replace('.',',',1) and user.count('.') == 1:
#     print(" given input is float ")
# elif user.lower() in [True,False]:
#     print(" givenn value is boolen ")
# else:
#     print(" given data is string")

# n = 10
# i = 1
# while i <= n:
#     print(i,end=" ")
#     i += 1

# n = 7 
# sum = 0
# for i in range(1,n+1):
#     if i % 2 == 1:
#         sum += i
# print(sum)

#number = [1,2,3,4,5,6,745]
#print(number.count(6))

#print(len(number))


# a = [1,2,3,4,5]
# print(a[0])
# print(a[-1])


# num = input(" enter a number ")
# if num.isdigit():
#     print(num[0])
#     print(num[-1])
# else:
#     print(" it is not a number ")

# num = input("12345")
# print(num[0])
# print(num[-1])

# num = input(" enter a number ")
# if num.isdigit():
#     total = sum(int(digit) for digit in num)
#     print(total)
# else:
#     print(" fuck you ")

# num = input(" enter a number ")
# if num.isdigit():
#     print(num[::-1])
        

# num = input(" enter  u want ")
# re = num[::-1]
# if re == num:
#     print("it is palindrome ")



# for i in range(32,128):
#     print(f" ascii {i} value {chr(i)}")




# num = 36
# for i in range(1,num+1):
#     if num % i == 0:
#         print(i,end=" ")

# num = 7
# count = 0
# for i in range(1,num+1):
#     if num%i == 0:
#         count+=1
# if count == 2:
#     print(" given number is prime number ",num)
# else: 
#     print(" given number is not prime number ",num)


# n = int(input(" enter a number "))
# for i in range(1,n+1):
#     if n == i*i:
#         print(" perfect square of ",i)



# def fibonacci(num):
#     a,b = 0,1
#     for _ in range(num):
#         print(a,end=" ")
#         a,b = b,a+b

# num = int(input("enter a numbers "))
# print(fibonacci(num))

# g = [1,23,434,23,334]
# print(max(g))


# g = [12,2,33,42,343,234,234,2,24]
# g.sort()
# print(g[-2]) 

# def function(st):
#     odd = []
#     even = []

#     for i in range(len(st)):
#         if i % 2 == 0:
#             even.append(st)
#         else:
#             odd.append(st)

#     return odd ,even

# number = [1,2,3,4,5,6,7,8]
# odd,even = function(number)
# print("even ",even)
# print("odd ",odd)

# g = [1,2,3,4,5,6,7]
# h = [4,5,6,7,8,9,0]
# f = g+h
# print(f)
# f.sort()
# print(f)




# import cmath
# a = 1
# b = 2
# c = 3
# delta = b**2-4*a*c
# sol1 = (-b-cmath.sqrt(delta))/(2*a)
# sol2 = (-b-cmath.sqrt(delta))/(2*a)
# print(f" sol1 : {sol1} sol2 : {sol2}")

# a = 10 
# b = 9
# a,b = b,a
# print(a,b)


# cel = 43
# fahre = (9/5)*cel+32
# print(fahre)



# def calc(a,b,c,):
#     if a == b == c:
#         return 3*(a+b+c)
    
# a = 2
# b = 2
# c = 2
# print(calc(a,b,c))


# year = int(input(" enter a year "))
# if year % 4 == 0:
#     print(" year is leap year ")
# else:
#     print(" year is not leap year ")


# num = 156
# if 100 < num <= 1000:
#     print(" number is btw 100 to 1000 ")
# else:
#     print(" number is btw the 1000  to 2000 ")



# a = 'k'

# if a.isascii():
#     print(" it is an alphabet ",a)
# else:
#     print(" its not a ascii value ")


# k = input(" enter a something ")

# if k.isdigit():
#     print(" given is a integer ",k)
# elif k.isalpha():
#     print(" it is alpha value ",k)
# else:
#     print(" it is an special  value ")



# weekday = [ ' ','sunday','monday','tuesday','wednesday','thursday','friday','saturday']
# print(weekday[5])


# amount = 10000

# if amount % 2000 == 0:
#     print(" 2000 notes is ",amount/2000)
# elif amount % 500 == 0:
#     print("500 notes ",amount/500)
# elif amount % 200 == 0:
#     print(" 200 notes ",amount/200)


# amount = 10570
# t2000 = amount%2000
# n2000 = amount/2000
# t500 = t2000%500
# n500 = t2000/500
# t200 = t500%200
# n200 = t500/200
# print(f"2000 {n2000} 500 {n500} 200 {n200}")


# a = input(" aravind ")
# if a.isalpha():
#     if a.isupper():
#         print(" it is upper ")
#     else :
#         print(" it is a lower ")
# else:
#     print(" it is not alphabet ")



# def digit_quency(num):
#     num_str = str(abs(num))


#     frequency = {}

#     for digit in num_str:
#         if digit in frequency:
#             frequency[digit] +=1
#         else:
#             frequency[digit] +=1

#     for digit, count in frequency.items():
#         print(f" digits : {digit} count : {count}")
# num = 11122323323
# digit_frequency(num)



# num = 1212121234345356

# def count(num):
#     freq = {}
#     num1 = str(num)
#     for ele in num1:
#         if int(ele) in freq:
#             freq[int(ele)] += 1
#         else:
#             freq[int(ele)] = 1
#         return freq

# print(count(num))


# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#        fact *= i
#     print(fact)

# print(factorial(5))





# def fibonacci(n):
#     a,b = 0,1
#     for i in range(n):
#         print(a,end=" ")
#         a,b = b,a+b

# fibonacci(10)





