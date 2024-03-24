def func(*args):
	ret_values = []
	
	import sys
	sys.setrecursionlimit(10000000)
	
	def solve():
	    (n, m, a, b) = rv()
	    a -= 1
	    b -= 1
	    if (((a // m) == (b // m)) or (m == 1)):
	        ret_values.append(1)
	        return
	    first = (m - (a - ((a // m) * m)))
	    last = ((b - ((b // m) * m)) + 1)
	    if ((b + 1) == n):
	        last = m
	    if ((first == m) and (last == m)):
	        ret_values.append(1)
	        return
	    if ((((a // m) + 1) == (b // m)) or ((first + last) == m)):
	        ret_values.append(2)
	        return
	    if ((first == m) or (last == m)):
	        ret_values.append(2)
	        return
	    ret_values.append(3)
	
	def prt(l):
	    return ret_values.append(' '.join(l))
	
	def rv():
	    return map(int, args[0].split())
	
	def rl(n):
	    return [list(map(int, args[1].split())) for _ in range(n)]
	if (sys.hexversion == 50594544):
	    sys.stdin = open('test.txt')
	solve()

	return ret_values
