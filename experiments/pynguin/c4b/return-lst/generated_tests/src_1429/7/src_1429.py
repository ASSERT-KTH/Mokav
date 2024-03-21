def func(*args):
	ret_values = []
	
	import sys
	
	def solve():
	    (a, b) = map(int, args[0].split())
	    (c, d) = map(int, args[1].split())
	    if (b < d):
	        (a, c) = (c, a)
	        (b, d) = (d, b)
	    for i in range(c):
	        if ((((b - d) + (i * a)) % c) == 0):
	            ans = (b + (i * a))
	            ret_values.append(ans)
	            return
	    ret_values.append((- 1))
	if (__name__ == '__main__'):
	    solve()

	return ret_values
