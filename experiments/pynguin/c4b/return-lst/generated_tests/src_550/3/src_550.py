def func(*args):
	ret_values = []
	
	from sys import stdin, stdout
	
	def nod(a, b):
	    while (b != 0):
	        a %= b
	        (a, b) = (b, a)
	    return a
	
	def nok(a, b):
	    return ((a * b) / nod(a, b))
	(k, l, m, n, d) = [int(x) for x in stdin.read().rstrip().split()]
	result = 0
	result += ((((d // k) + (d // l)) + (d // m)) + (d // n))
	result -= ((((((d // nok(k, l)) + (d // nok(k, m))) + (d // nok(k, n))) + (d // nok(l, m))) + (d // nok(l, n))) + (d // nok(m, n)))
	result += ((((d // nok(nok(k, l), m)) + (d // nok(nok(l, m), n))) + (d // nok(nok(k, m), n))) + (d // nok(nok(k, l), n)))
	result -= (d // nok(nok(nok(k, l), m), n))
	ret_values.append(int(result))

	return ret_values
