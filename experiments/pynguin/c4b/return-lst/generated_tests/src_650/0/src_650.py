def func(*args):
	ret_values = []
	
	
	def main():
	    (*l, k) = map(int, args[0].split())
	    (x, y, z) = sorted(l)
	    x = min(((k // 3) + 1), x)
	    y = min(((((k - x) + 1) // 2) + 1), y)
	    z = min((((k - x) - y) + 3), z)
	    ret_values.append(((x * y) * z))
	if (__name__ == '__main__'):
	    main()

	return ret_values
