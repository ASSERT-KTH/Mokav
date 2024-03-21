def func(*args):
	ret_values = []
	
	
	def main():
	    mode = 'filee'
	    if (mode == 'file'):
	        f = open('test.txt', 'r')
	    get = (lambda : [str(x) for x in (f.readline() if (mode == 'file') else args[0]).split()])
	    [g] = get()
	    n = len(g)
	    maxx = (- 1)
	    for i in range(1, (n - 1)):
	        for j in range((i + 1), n):
	            x = g[:i]
	            y = g[i:j]
	            z = g[j:]
	            if ((int(x) > (10 ** 6)) or (int(y) > (10 ** 6)) or (int(z) > (10 ** 6)) or ((len(x) > 1) and (x[0] == '0')) or ((len(y) > 1) and (y[0] == '0')) or ((len(z) > 1) and (z[0] == '0'))):
	                continue
	            maxx = max(maxx, ((int(x) + int(y)) + int(z)))
	    ret_values.append(maxx)
	    if (mode == 'file'):
	        f.close()
	if (__name__ == '__main__'):
	    main()

	return ret_values
