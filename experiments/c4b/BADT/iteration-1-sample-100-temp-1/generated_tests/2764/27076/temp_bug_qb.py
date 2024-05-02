def original_func(*args):
	global_list = []
	
	a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
	z = ([0] * len(a))
	(n, k) = map(int, args[0].split())
	old = n
	i = 0
	while True:
	    if (n == 1):
	        break
	    if (i == len(a)):
	        break
	    if ((n % a[i]) == 0):
	        n //= a[i]
	        z[i] += 1
	    else:
	        i += 1
	i = 0
	ans = ''
	p = 1
	x = 0
	while (i < len(a)):
	    if (z[i] == 0):
	        i += 1
	    else:
	        x += 1
	        if (x == k):
	            break
	        p *= a[i]
	        ans += (str(a[i]) + ' ')
	        z[i] -= 1
	if (x == k):
	    global_list.append((ans + str((old // p))))
	elif ((x == (k - 1)) and ((old // p) != 1)):
	    global_list.append((ans + str((old // p))))
	else:
	    global_list.append((- 1))
	return global_list