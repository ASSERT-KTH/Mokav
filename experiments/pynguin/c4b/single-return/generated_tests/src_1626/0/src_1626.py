def func(*args):
	
	s = args[0]
	z = ['R', 'B', 'Y', 'G']
	r = s.find('R')
	ans = [0, 0, 0, 0]
	for i in range(4):
	    r = s.find(z[i])
	    while ((r - 4) >= 0):
	        r -= 4
	    while (r <= (len(s) - 1)):
	        j = r
	        if (s[j] != z[i]):
	            ans[i] += 1
	        r += 4
	ans = map(str, ans)
	return(' '.join(ans))
