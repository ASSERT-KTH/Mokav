def func(*args):
	
	
	def main():
	    (x, y) = map(int, args[0].split())
	    max_q = (- 1)
	    (a, b) = (x, y)
	    while (x > 0):
	        max_q = max(max_q, (x % 10))
	        x = (x // 10)
	    while (y > 0):
	        max_q = max(max_q, (y % 10))
	        y = (y // 10)
	    max_q = (max_q + 1)
	    k = 0
	    z = (int(str(a), max_q) + int(str(b), max_q))
	    while (z > 0):
	        k += 1
	        z = (z // max_q)
	    return(k)
	if (__name__ == '__main__'):
	    main()
