import math
p = input("Enter Perimeter")

triangles = list()

counter = 0
for o in range(1, p):
	for a in range(1, p):
		for h in range(1, p):
			if o < a + h and a < o + h and h < a + o and a + o + h == p:
				#print(str(o) +" "+ str(a) +" "+ str(h))
				arr = list()
				arr.append(o)
				arr.append(a)
				arr.append(h)
				arr.sort()
				#print(arr)
				
				if not arr in triangles:
					#print(arr)
					triangles.append(arr)
				counter += 1
					
print(len(triangles))
#print(counter)