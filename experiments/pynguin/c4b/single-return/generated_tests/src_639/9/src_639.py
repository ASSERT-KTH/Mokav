def func(*args):
	
	
	def f(lim):
	    (four, seven, seed, base, l) = (4, 7, 0, 1, [0])
	    while True:
	        cur = l[(base - 1):]
	        for head in (four, seven):
	            for seed in cur:
	                seed += head
	                l.append(seed)
	                if (seed >= lim):
	                    return l
	        four *= 10
	        seven *= 10
	        base *= 2
	
	def main():
	    (lo, hi) = map(int, args[0].split())
	    l = f(hi)
	    res = a = 0
	    for b in l:
	        res += ((b - a) * b)
	        a = b
	    res -= ((b - hi) * b)
	    a = 0
	    for b in l:
	        res -= ((b - a) * b)
	        if (b >= lo):
	            break
	        a = b
	    return((res + (((b - lo) + 1) * b)))
	if (__name__ == '__main__'):
	    main()
