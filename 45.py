import math
	
n = 143;
	
while True:
	n += 1
	x = (math.sqrt(24*n*(2*n-1)+1) + 1) / 6.0
	if math.floor(x) == x:
		break

print( n*(2*n-1) )