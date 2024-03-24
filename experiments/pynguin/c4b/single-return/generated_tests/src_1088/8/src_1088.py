def func(*args):
	
	import math
	(n, red, blue, red_cost, blue_cost) = map(int, args[0].split())
	reds = (n // red)
	blues = (n // blue)
	ans = (((reds * red_cost) + (blues * blue_cost)) - (min(blue_cost, red_cost) * (n // ((red * blue) // math.gcd(red, blue)))))
	return(int(ans))
