def func(*args):
	ret_values = []
	
	import math
	
	def main():
	    n = int(args[0])
	    phib = [1, 1]
	    ans = 0
	    while ((phib[(- 1)] + phib[(- 2)]) <= n):
	        phib.append((phib[(- 1)] + phib[(- 2)]))
	        ans += 1
	    ret_values.append(ans)
	main()

	return ret_values
