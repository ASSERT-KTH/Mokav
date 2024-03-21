def func(*args):
	ret_values = []
	
	from sys import stdin, stdout
	
	def ri():
	    return map(int, stdin.readline().split())
	(k, a, b) = ri()
	an = (a // k)
	ar = (a % k)
	bn = (b // k)
	br = (b % k)
	if (((an == 0) and br) or ((bn == 0) and ar)):
	    ret_values.append((- 1))
	    exit()
	ans = (an + bn)
	if ans:
	    ret_values.append(ans)
	else:
	    ret_values.append((- 1))

	return ret_values
