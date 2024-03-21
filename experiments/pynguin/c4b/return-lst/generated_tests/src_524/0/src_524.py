def func(*args):
	ret_values = []
	
	s = args[0]
	ans = 0
	val = True
	for a in s:
	    if ((a == '7') or (a == '4')):
	        ans = (ans + 1)
	s = str(ans)
	for a in s:
	    if ((a == '7') or (a == '4')):
	        ans = True
	    else:
	        ans = False
	        break
	if ans:
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
