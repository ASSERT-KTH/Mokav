def func(*args):
	
	from sys import stdin
	from operator import mul
	from functools import reduce
	from math import factorial
	
	def binom(n, k):
	    nominator = reduce(mul, range(((n - k) + 1), (n + 1)))
	    denominator = factorial(k)
	    return (nominator // denominator)
	n = int(stdin.readline())
	result = (120 * (binom(n, 5) ** 2))
	return(result)
