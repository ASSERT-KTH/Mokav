def func(*args):
	
	import math
	from queue import *
	
	def norecursivo(n, l, r):
	    cola = Queue()
	    h = (log2(n) + 1)
	    m = (cantnodos(h) if (h > 2) else 0)
	    cola.put((n, m))
	    cont = 0
	    while (not cola.empty()):
	        (n, pos) = cola.get()
	        if ((pos >= l) and (pos <= r) and ((n % 2) == 1)):
	            cont += 1
	        h = (log2(n) + 1)
	        m = (cantnodos((h - 1)) if (h > 2) else 0)
	        if (h > 1):
	            if (pos > l):
	                cola.put(((n >> 1), ((pos - m) - 1)))
	            if (pos < r):
	                cola.put(((n >> 1), ((pos + m) + 1)))
	    return cont
	
	def log2(n):
	    iteraciones = 0
	    cociente = n
	    while (cociente > 0):
	        cociente = (cociente >> 1)
	        iteraciones = (iteraciones + 1)
	    return iteraciones
	
	def cantnodos(h):
	    return (pow(2, (h - 2)) - 1)
	(n, l, r) = [int(n) for n in args[0].split()]
	cont = norecursivo(n, (l - 1), (r - 1))
	return(cont)
