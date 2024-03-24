def func(*args):
	ret_values = []
	
	'http://codeforces.com/problemset/problem/219/B'
	if (__name__ == '__main__'):
	    (p, d) = map(int, args[0].split())
	    lo = (p - d)
	    res = p
	    for i in range(1, 18):
	        num = (10 ** i)
	        t = (((p // num) * num) + (num - 1))
	        t = (t if (t <= p) else (t - num))
	        if ((p - t) <= d):
	            res = t
	        else:
	            break
	    ret_values.append(res)

	return ret_values
