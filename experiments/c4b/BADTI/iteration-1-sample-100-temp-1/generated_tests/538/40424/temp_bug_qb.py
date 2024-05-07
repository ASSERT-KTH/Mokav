def original_func(*args):
	global_list = []
	
	arr = [int(i) for i in args[0].split()]
	hsh = [0 for i in range(0, 101)]
	arr.sort()
	for i in arr:
	    hsh[i] += 1
	i = 4
	while (i >= 0):
	    if (hsh[arr[i]] >= 3):
	        hsh[arr[i]] -= 3
	        break
	    elif (hsh[arr[i]] >= 2):
	        hsh[arr[i]] -= 2
	        break
	    i -= 1
	ans = 0
	i = 0
	for i in range(0, 101):
	    ans += (hsh[i] * i)
	global_list.append(ans)
	return global_list