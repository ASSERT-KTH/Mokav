def func(*args):
	ret_values = []
	
	
	def main():
	    (a, b, c) = map(int, args[0].split())
	    min_a = min(a, b)
	    max_a = max(a, b)
	    for i in range(((c // min_a) + 1)):
	        if (((c - (min_a * i)) % max_a) == 0):
	            return 'Yes'
	    return 'No'
	ret_values.append(main())

	return ret_values
