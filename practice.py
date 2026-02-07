# s = "sms"
# if(s==(s[::-1])):
#     print("palindrome")
# else:
#     print("notPalindrome")/

# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) +fib(n-2)

# n = 6
# print(fib(n))

# def prime(n):
#     count = 0
#     if n <= 1:
#         return 1
#     else:
#         for i in range(2,n+1):
#             if n % i == 0:
#                 count += 1
#         if(count == 1):
#             return "Prime"
#         else:
#             return "NotPrime"
        
# n = 6
# print(prime(n))



# arr = [5,1,3,2,1,0]
# arr.sort()
# arr.pop(1)
# print(arr)
# print(arr[::-1])


# arr = [5,1,3,2,5,0,0]
# arr.sort()
# print(arr)
# for i in range(len(arr) - 1 ):
#     if(arr[i] == arr[i-1]):
#         arr.pop(i)
# print(arr)


# def Anagram(s1,s2):
#     if(sorted(s1)== sorted(s2)):
#         return "Anagram"
#     else:
#         return "Its Not"
    
# s1 = "hello"
# s2 = "ellohs" 
# print(Anagram(s1,s2))

# s1 = "hello"
# s2 = sorted(s1)
# print(s2)
# count = 0
# for i in range(len(s2) -1):
#     for j in range(i+1,len(s2) -1):
#         if(s2(i) == s2(j)):
#             count += count
#     print(s2(i),count)

# from collections import Counter
# s = "hello"
# print((Counter(s)))
# print(dict(Counter(s)))


# s1 = "hello"
# freq = {}
# for char in s1:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1
# print(freq)


# def fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     return fact

# print(fact(5))




# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print(fact)


# def BinarySearch(arr,target):
#     left,right = 0,len(arr)-1
#     while left <= right:
#         mid = (right + left)//2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] <target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# arr = [1,9,3,5,3,5,7,8]
# target = 9
# arr.sort()
# print(arr)
# print(BinarySearch,target)



# def armstrong(n):
#     return sum(int(d)**3 for d in str(n)) == n

# print(armstrong(153))
# print(armstrong(121))

# arr = [1,1,2,3,2,3,4,4]
# arr1 = list(set(arr))
# print(arr1)
# print(list(dict.fromkeys(arr)))

# def Sum(n):
#     return sum(int(i) for i in range(n+1))

# print(Sum(5))

# def leapyear(n):
#     return (n%4==0 and n%100!=0) or (n%400 == 0)

# print(leapyear(1892))


# def Vowels(s):
#     return sum(1 for ch in s.lower() if ch in "aeiou")

# print(Vowels("Education"))

# def Max(arr):
#     return max(arr)
# arr = [1,2,3,4,5,6,7,9]
# print(Max(arr))


# def Max(arr):
#     arr.sort
#     return arr[-1]

# arr = [1,2,3,4,5,6,8,9]
# print(Max(arr))
# print(arr[:-1])

# def Even(n):
#     return ("Even" if n%2 == 0 else "odd")

# print(Even(349))


# def Sum(n):
#     return sum(i for i in range(n+1) if i > 0 )

# print(Sum(5))

# import math
# n = 26
# b = int(math.sqrt(n))

# if(b**2 == n):
#     print("Perfect Square ")
# else:
#     print("Not perfect Square ")





# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print(fact)


# def Fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     return fact

# n = int(input("enter a variable "))
# print(Fact(5))

"""
import sys

print(sys.version)"""