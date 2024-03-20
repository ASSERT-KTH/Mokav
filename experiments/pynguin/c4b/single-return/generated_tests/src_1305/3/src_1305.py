def func(*args):
	
	from itertools import permutations
	
	def findPow(num):
	    ans = 1
	    num = (num // 7)
	    while (num > 0):
	        num //= 7
	        ans += 1
	    return ans
	(a, b) = [int(x) for x in args[0].split(' ')]
	x = findPow((a - 1))
	y = findPow((b - 1))
	ans = 0
	if ((x + y) > 7):
	    ans = 0
	else:
	    for i in permutations('0123456', (x + y)):
	        s = ''.join(list(i))
	        (p, q) = (int(s[:x], 7), int(s[x:], 7))
	        if ((p <= (a - 1)) and (q <= (b - 1))):
	            ans += 1
	return(ans)
