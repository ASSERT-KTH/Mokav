def func(*args):
	
	s = args[0]
	ans = 0
	c = 0
	for i in s:
	    c += 1
	    if ((i == 'A') or (i == 'E') or (i == 'I') or (i == 'O') or (i == 'U') or (i == 'Y')):
	        if (c > ans):
	            ans = c
	        c = 0
	if ((c + 1) > ans):
	    ans = (c + 1)
	return(ans)
