def func(*args):
	ret_values = []
	
	(a, b) = list(map(int, args[0].split()))
	c = max(a, b)
	ans = 0
	for i in range((c + 1)):
	    for j in range((c + 1)):
	        if ((((i ** 2) + j) == a) and ((i + (j ** 2)) == b)):
	            ans += 1
	ret_values.append(ans)

	return ret_values
