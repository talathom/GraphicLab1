import math
def perfect(n):
	sum = 0
	for i in range(1, n):
		if n % i == 0:
			print(i)
			sum += i
	if n == sum:
		return True
	else:
		return False
		
n = input("Input a Number")
print(str(perfect(n)))
			