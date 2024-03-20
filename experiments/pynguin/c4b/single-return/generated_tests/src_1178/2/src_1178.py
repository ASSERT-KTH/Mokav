def func(*args):
	
	MAX = 100005
	
	def big_pow3(n):
	    l = 0
	    p = MAX
	    while ((p - l) != 1):
	        mid = (((p + l) + 1) // 2)
	        if (((mid * mid) * mid) <= n):
	            l = mid
	        else:
	            p = mid
	    return l
	
	def f(n):
	    if (n < 8):
	        return [n, n]
	    a = int(((n + 0.5) ** 0.3333333333333333))
	    r1 = f((n - (a ** 3)))
	    r1 = [(r1[0] + 1), (r1[1] + (a ** 3))]
	    a -= 1
	    r2 = f(((3 * a) * (a + 1)))
	    r2 = [(r2[0] + 1), (r2[1] + (a ** 3))]
	    return max(r1, r2)
	if (__name__ == '__main__'):
	    m = int(args[0])
	    return(*f(m))
