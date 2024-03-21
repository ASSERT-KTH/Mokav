def func(*args):
	ret_values = []
	
	s = list(args[0])
	b = []
	ans = 0
	i = 1
	while (i < len(s)):
	    if ((s[i] == 'K') and (s[(i - 1)] == 'V')):
	        ans += 1
	        b.append(i)
	        b.append((i - 1))
	        i += 2
	    else:
	        i += 1
	i = 1
	while (i < len(s)):
	    if ((((s[i] == 'V') and (s[(i - 1)] == 'V')) or ((s[i] == 'K') and (s[(i - 1)] == 'K'))) and ((b.count(i) == 0) and (b.count((i - 1)) == 0))):
	        ans += 1
	        break
	    else:
	        i += 1
	ret_values.append(ans)

	return ret_values
