def func(*args):
	
	
	def solve():
	    (n, m) = map(int, args[0].split())
	    stop_yn = True
	    while stop_yn:
	        for i in range(1, (n + 1)):
	            if ((m - i) >= 0):
	                m -= i
	            else:
	                stop_yn = False
	    return(m)
	if (__name__ == '__main__'):
	    solve()
