def func(*args):
	
	s = args[0]
	count = 0
	ans = 1
	for i in range(1, len(s)):
	    if ((count == 4) or ((count <= 4) and (s[i] != s[(i - 1)]))):
	        count = 0
	        ans += 1
	    elif (s[i] == s[(i - 1)]):
	        count += 1
	    if ((s[i] != s[(i - 1)]) and (count != 0)):
	        ans += 1
	        count = 0
	return(ans)
