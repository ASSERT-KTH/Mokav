def func(*args):
	ret_values = []
	
	
	def main():
	    (a, b, c) = (int(n) for n in args[0].split())
	    (x, y, z) = (int(n) for n in args[1].split())
	    if solver(a, b, c, x, y, z):
	        ret_values.append('Yes')
	    else:
	        ret_values.append('No')
	
	def solver(a, b, c, x, y, z):
	    if ((a >= x) and (b >= y) and (c >= z)):
	        return True
	    elif ((a >= x) and (b >= y) and (c < z)):
	        return ((((a - x) // 2) + ((b - y) // 2)) >= (z - c))
	    elif ((a >= x) and (b < y) and (c >= z)):
	        return ((((a - x) // 2) + ((c - z) // 2)) >= (y - b))
	    elif ((a < x) and (b >= y) and (c >= z)):
	        return ((((b - y) // 2) + ((c - z) // 2)) >= (x - a))
	    elif ((a < x) and (b < y) and (c >= z)):
	        return (((c - z) // 2) >= (((x - a) + y) - b))
	    elif ((a < x) and (b >= y) and (c < z)):
	        return (((b - y) // 2) >= (((x - a) + z) - c))
	    elif ((a >= x) and (b < y) and (c < z)):
	        return (((a - x) // 2) >= (((y - b) + z) - c))
	    else:
	        return False
	main()

	return ret_values
