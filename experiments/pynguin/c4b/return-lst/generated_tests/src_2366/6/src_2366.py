def func(*args):
	ret_values = []
	
	'http://codeforces.com/problemset/problem/233/B'
	
	def s(x):
	    return sum(map(int, str(x)))
	
	def val(x):
	    return ((x * x) + (s(x) * x))
	
	def solve(n):
	    l = 1
	    r = (int((n ** 0.5)) + 1)
	    while (l <= r):
	        mid = ((l + r) // 2)
	        ret_values.append(l, mid, r, val(mid))
	        if (val(mid) == n):
	            return mid
	        elif ((mid ** 2) < n):
	            l = (mid + 1)
	        elif ((mid ** 2) > n):
	            r = (mid - 1)
	    return (- 1)
	
	def solve2(n):
	    for sx in range(1, 81):
	        x = int((((- sx) + (((sx ** 2) + (4 * n)) ** 0.5)) // 2))
	        if ((s(int(x)) == sx) and ((x * (x + sx)) == n)):
	            return x
	    return (- 1)
	
	def test():
	    assert (solve2(4) == (- 1))
	if (__name__ == '__main__'):
	    test()
	    ret_values.append(solve2(int(args[0])))

	return ret_values
