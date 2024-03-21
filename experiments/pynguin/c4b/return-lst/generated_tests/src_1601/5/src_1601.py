def func(*args):
	ret_values = []
	
	(n, k) = args[0].split()
	k = int(k)
	ans = 0
	count = 0
	for num in n[::(- 1)]:
	    if (count == k):
	        ret_values.append(ans)
	        exit()
	    if (num == '0'):
	        count += 1
	    if (num != '0'):
	        ans += 1
	ret_values.append(((ans + count) - 1))

	return ret_values
