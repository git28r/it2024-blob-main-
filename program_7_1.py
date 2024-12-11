d = int(input())
x = int(input())

a =int((((365-(75/(d*d*d)))/(3*(d*d)-d))*5)*x)
print(a)

b = int((((412-125/(d*d*d))/(2*(d*d)-d))*4)*x)
print(b)
sum = (a+b)
print(sum)


