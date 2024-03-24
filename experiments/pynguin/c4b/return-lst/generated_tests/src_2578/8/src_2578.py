def func(*args):
	ret_values = []
	
	
	def main():
	    (n, m, k) = (int(t) for t in args[0].split())
	    if ((n % 2) == 0):
	        ret_values.append('Marsel')
	        return
	    if ((k == 1) and (m > k)):
	        ret_values.append('Timur')
	        return
	    t = 2
	    while ((t * t) <= m):
	        if ((m % t) == 0):
	            if ((m // t) >= k):
	                ret_values.append('Timur')
	                return
	            ret_values.append('Marsel')
	            return
	        t += 1
	    ret_values.append('Marsel')
	    return
	main()

	return ret_values
