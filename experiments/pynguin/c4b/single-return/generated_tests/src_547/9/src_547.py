def func(*args):
	
	
	def triangle(a0, a1, a2, a3):
	
	    def t(a0, a1, a2):
	        if ((a0 < (a1 + a2)) and (a1 < (a0 + a2)) and (a2 < (a0 + a1))):
	            return 1
	        else:
	            return 0
	
	    def s(a0, a1, a2):
	        if ((a0 == (a1 + a2)) or (a1 == (a0 + a2)) or (a2 == (a0 + a1))):
	            return 1
	        else:
	            return 0
	
	    def i(a0, a1, a2):
	        if ((a0 > (a1 + a2)) or (a1 > (a2 + a0)) or (a2 > (a0 + a1))):
	            return 1
	        else:
	            return 0
	    if (t(a0, a1, a2) or t(a1, a2, a3) or t(a0, a1, a3) or t(a0, a2, a3)):
	        return 'TRIANGLE'
	    elif (s(a0, a1, a2) or s(a1, a2, a3) or s(a0, a1, a3) or s(a0, a2, a3)):
	        return 'SEGMENT'
	    elif (i(a0, a1, a2) or i(a1, a2, a3) or i(a0, a1, a3) or i(a0, a2, a3)):
	        return 'IMPOSSIBLE'
	(a0, a1, a2, a3) = map(int, args[0].split())
	return(triangle(a0, a1, a2, a3))
