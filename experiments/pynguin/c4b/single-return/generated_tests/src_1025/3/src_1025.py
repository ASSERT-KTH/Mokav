def func(*args):
	
	n = 0
	s = ''
	
	def check():
	    global n
	    global s
	    t = 0
	    for i in range(0, (len(s) // 2)):
	        t *= 10
	        t += 7
	    for i in range(0, (len(s) // 2)):
	        t *= 10
	        t += 4
	    if (int(s) > t):
	        n += 2
	
	def rec(i):
	    global n
	    global s
	    j = ((i * 10) + 4)
	    k = ((i * 10) + 7)
	    (f1, f2) = (False, False)
	    if (len(str(j)) == n):
	        if ((j >= int(s)) and (str(j).count('4') == str(j).count('7'))):
	            f1 = True
	        if ((k >= int(s)) and (str(k).count('4') == str(k).count('7'))):
	            f2 = True
	        if (f1 and f2):
	            return min(k, j)
	        elif f1:
	            return j
	        elif f2:
	            return k
	        else:
	            return 1000000000000000.0
	    return min(rec(k), rec(j))
	s = args[0]
	n = (len(s) + int(((len(s) % 2) != 0)))
	if ((len(s) % 2) == 0):
	    check()
	return(rec(0))
