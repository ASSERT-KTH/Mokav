def func(*args):
	
	
	def nod(m):
	    list1 = [1, 3, 5, 7, 8, 10, 12]
	    if (m in list1):
	        return 31
	    else:
	        return 30
	
	def solve(m, d):
	    if (m == 2):
	        if (d == 1):
	            return 4
	        return 5
	    elif (nod(m) == 30):
	        if (d == 7):
	            return 6
	        else:
	            return 5
	    elif ((d == 6) or (d == 7)):
	        return 6
	    else:
	        return 5
	(m, d) = args[0].strip().split(' ')
	(m, d) = (int(m), int(d))
	return(solve(m, d))
