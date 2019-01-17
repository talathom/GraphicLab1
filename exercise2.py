dollars = input("How much change is needed")

twenties = 0
tens = 0
fives = 0
ones = 0

while dollars > 0:
	if dollars % 20 == 0:
		twenties += 1
		dollars -= 20
	elif dollars % 10 == 0:
		tens += 1
		dollars -= 10
	elif dollars % 5 == 0:
		fives += 1
		dollars -= 5
	else:
		ones += 1
		dollars -= 1
		
print(twenties, " twenties")
print(tens, " tens")
print(fives, " fives")
print(ones, " ones")