def patched_func(*args):
	global_list = []
	
	
	def main():
	    (n, m, k) = (int(t) for t in args[0].split())
	    if ((n % 2) == 0):
	        global_list.append('Marsel')
	        return
	    if ((k == 1) and (m > k)):
	        global_list.append('Timur')
	        return
	    t = 2
	    while ((t * t) <= m):
	        if ((m % t) == 0):
	            if ((m // t) >= k):
	                global_list.append('Timur')
	                return
	            global_list.append('Marsel')
	            return
	        t += 1
	    global_list.append('Marsel')
	    return
	main()
	return global_list