def func(*args):
	ret_values = []
	
	__author__ = 'Darren'
	
	def solve():
	    from math import ceil
	    x = abs(int(args[0]))
	    k = ceil((((((8 * x) + 1) ** 0.5) - 1) / 2))
	    location = ((k * (k + 1)) // 2)
	    if ((location == x) or (((location - x) % 2) == 0)):
	        ret_values.append(k)
	    elif ((((location - x) + (k + 1)) % 2) == 0):
	        ret_values.append((k + 1))
	    else:
	        ret_values.append((k + 2))
	if (__name__ == '__main__'):
	    solve()

	return ret_values
