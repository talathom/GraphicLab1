import math

def isPrime(n):
	if n % 2 == 0:
		return False
	#Start 3, going to square root of n which is greatest possible divisor, increments by 2
	for i in range(3, int(round(math.sqrt(n))), 2):
		if n % i == 0:
			return False
	return True

n = input("Enter a number")
if isPrime(n):
	print(str(n) +" is Prime")
else:
	print(str(n) +" is not Prime")

	