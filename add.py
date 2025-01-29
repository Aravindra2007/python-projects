amount = int(input(" enter a amount  "))
type = input(" enter type of membership ")
if type == "gold":
    discount = 0.5
    total = amount - amount*discount
    print(" total amount is ",total)
elif type == "silver":
    discount = 0.15
    total = amount - amount*discount
    print(" tota; dicount is ",total)
else:
    discount = 0.1
    total = amount - amount*discount
    print("total  amount is ",total)



n = int(input(" emter a number "))
for i in range(1,n+1):
    harm = 1/i
    i+=1
    print(harm,end=" + ")




a = int(input(" enter a value "))
b = int(input(" enter b value "))
sum = a+b
sub = a-b
mul = a*b
div = a/b
print(sum,sub,mul,div)
print(" in float values ")
print(float(sum))
print(float(sub))
print(float(mul))
print(float(div))


a = 10
b = 5
type = input(" enter the type operator ")
if type == "and":
    c = a&b
    print(c)
elif type == "or":
    c = a|b
    print(c)
elif type == "xor":
    c = ~a
    print(c)
elif type == "not":
    c = a
    print(c)