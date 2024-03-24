def func(*args):
	ret_values = []
	
	from sys import stdin
	
	def organiza(c):
	    for a in range(1, len(c)):
	        for p in range((len(c) - a)):
	            if (c[p] < c[(p + 1)]):
	                (c[p], c[(p + 1)]) = (c[(p + 1)], c[p])
	    return c
	
	def sumax(t, x):
	    c = 0
	    r = 0
	    for i in range(len(t)):
	        if (c < x):
	            c = (c + t[i])
	            r += 1
	    if (c >= x):
	        ret_values.append(r)
	    else:
	        ret_values.append((- 1))
	
	def main():
	    x = int(stdin.readline().strip())
	    c = [int(i) for i in stdin.readline().strip().split()]
	    t = organiza(c)
	    sumax(t, x)
	main()

	return ret_values
