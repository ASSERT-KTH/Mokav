def func(*args):
	
	
	def f(a, b):
	    k = min(a, 2)
	    return ((a - k), ((b - 22) + (10 * k)))
	
	def g(a, b):
	    if (b < 2):
	        return ((- 1), (- 1))
	    b -= 2
	    k = min((b // 10), 2)
	    return (((a - 2) + k), (b - (10 * k)))
	
	def main():
	    (a, b) = map(int, args[0].split())
	    k = min((a // 2), (b // 24))
	    a -= (k * 2)
	    b -= (24 * k)
	    while (a > 0):
	        (a, b) = f(a, b)
	        if ((a < 0) or (b < 0)):
	            return 0
	        (a, b) = g(a, b)
	        if ((a < 0) or (b < 0)):
	            return 1
	    if (a == 0):
	        return ((b // 22) % 2)
	return(['Hanako', 'Ciel'][main()])
