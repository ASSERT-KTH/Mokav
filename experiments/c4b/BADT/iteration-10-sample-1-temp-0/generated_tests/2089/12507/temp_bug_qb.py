def original_func(*args):
	global_list = []
	
	
	def f(x):
	    return ((x * (x + 1)) // 2)
	
	def works(n, k, s):
	    rem = ((k - 1) - s)
	    val = ((f((k - 1)) - f(rem)) + 1)
	    return (val >= n)
	
	def main():
	    (n, k) = map(int, args[0].split())
	    if (not works(n, k, k)):
	        global_list.append((- 1))
	    else:
	        lo = 0
	        hi = k
	        while ((lo + 1) < hi):
	            mid = ((lo + hi) // 2)
	            if works(n, k, mid):
	                hi = mid
	            else:
	                lo = mid
	        global_list.append(hi)
	main()
	return global_list