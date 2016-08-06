def add(num1,num2):
	return num1+num2

def subtract(num1,num2):
	return num1-num2

def multiply (num1,num2):
	return num1*num2

def divide (num1,num2):
	return num1/num2

def modulo (num1,num2):
	return num1%num2

def power (base,exponent):
	return base**exponent

def square (num):
	return power(num,2)

print add(add(4,5),subtract(9,6))

print subtract(divide(12,2),60)

print add(add(1,2),3)

print square(add(1,2))

print divide(modulo(3,4),multiply(9,9))

print multiply(7,add(3,8))

print subtract(add(1,2),multiply(3,add(4,5)))

print power(3,add(2,3))