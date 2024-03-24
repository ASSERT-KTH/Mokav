def func(*args):
	ret_values = []
	
	from math import log10
	(p, d) = [int(n) for n in args[0].split()]
	
	def getLargestWithKNines(p, k):
	    p = (p + 1)
	    return ((p - (p % (10 ** k))) - 1)
	
	def main():
	    maxK = int((log10(p) + 1))
	    for k in range(maxK, 0, (- 1)):
	        T = getLargestWithKNines(p, k)
	        if (((p - T) <= d) and (T >= 0)):
	            ret_values.append(T)
	            return
	    ret_values.append(p)
	    return
	main()

	return ret_values
