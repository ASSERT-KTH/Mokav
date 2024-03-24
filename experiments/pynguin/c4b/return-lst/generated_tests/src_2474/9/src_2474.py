def func(*args):
	ret_values = []
	
	import sys
	import math
	
	def primes(number):
	    size = (number + 1)
	    lst = ([True] * (number + 1))
	    primeList = []
	    for i in range(2, number):
	        if (lst[i] == False):
	            continue
	        for j in range((i * 2), size, i):
	            if ((j < size) and (lst[j] == True) and ((j % i) == 0)):
	                lst[j] = False
	    for i in range((size - 1), 0, (- 1)):
	        if (lst[i] == True):
	            primeList.append(i)
	    primeList.sort()
	    return primeList[1:]
	
	def solve(firstLine):
	    (n, k) = (firstLine[0], firstLine[1])
	    primeList = primes(((n * 2) + 1))
	    sol = 0
	    for (i, prime) in enumerate(primeList):
	        if (primeList[(i + 1)] > n):
	            break
	        num = ((primeList[(i + 1)] + primeList[i]) + 1)
	        if ((num <= n) and (num in primeList)):
	            sol += 1
	    if (sol >= k):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')
	    return
	
	def main():
	    firstLine = sys.stdin.readline().split()
	    firstLine = list(map(int, firstLine))
	    solve(firstLine)
	if (__name__ == '__main__'):
	    main()

	return ret_values
