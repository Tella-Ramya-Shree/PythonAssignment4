#Prime number or not
num = int(input("enter a number: "))
for i in range(2, num):
	if (num % i  == 0):
		print(num," is a not prime number")
		break
else:
	print(num,"is a prime number")