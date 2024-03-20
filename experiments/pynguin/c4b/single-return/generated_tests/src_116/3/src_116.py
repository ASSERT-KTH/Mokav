def func(*args):
	
	
	def dragon_injurd(k, l, m, n, d):
	    dragon = ([0] * d)
	    r = 0
	    injurd = [k, l, m, n]
	    for i in range(4):
	        r = 0
	        while (r <= (d - 1)):
	            if (((r + 1) % injurd[i]) == 0):
	                dragon[r] = 1
	            r += 1
	    return sum(dragon)
	
	def main():
	    k = int(args[0])
	    l = int(args[1])
	    m = int(args[2])
	    n = int(args[3])
	    d = int(args[4])
	    return(dragon_injurd(k, l, m, n, d))
	if (__name__ == '__main__'):
	    main()
