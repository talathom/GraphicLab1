def amount(bill, tax=0.07, tip=.15):
	return (bill * tax) + (bill * tip) + bill
	
print(amount(100))
print(amount(100, 0.03, .2))
print(amount(100, tip=0.1))
print(amount(100, tax=0.05))
print(amount(100, tip=0.12, tax=0.04))
#print(amount(100, tax=0.04, 0.10)) # Not last keyword bad
print(amount(100, 0.04, tip=0.10)) # Works as last