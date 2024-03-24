def func(*args):
	
	import math
	
	def luckyCheck(n):
	    a = 0
	    for char in str(n):
	        if (char not in ['4', '7']):
	            a = 1
	    if (a == 1):
	        return False
	    return True
	
	def luckyNum(n):
	    i = 2
	    a = n
	    primeList = []
	    while (i <= a):
	        while ((n % i) == 0):
	            n /= i
	            if (i not in primeList):
	                primeList.append(i)
	        i += 1
	    if (luckyCheck(a) == True):
	        return 'YES'
	    for prime in primeList:
	        if ((prime == 2) and (a >= 2)):
	            if ((a % 4) == 0):
	                return 'YES'
	        elif ((prime == 7) and (a >= 7)):
	            return 'YES'
	        if luckyCheck(prime):
	            return 'YES'
	    return 'NO'
	return(luckyNum(int(args[0])))
