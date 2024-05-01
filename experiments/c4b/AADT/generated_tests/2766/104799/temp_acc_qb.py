def patched_func(*args):
	global_list = []
	
	str = args[0]
	ls = len(str)
	(i, j, ans) = (0, (ls - 1), 0)
	while (i < j):
	    if (str[i] != str[j]):
	        ans = (ans + 1)
	    i = (i + 1)
	    j = (j - 1)
	if ((ans > 1) or ((ans == 0) and ((ls & 1) == 0))):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list