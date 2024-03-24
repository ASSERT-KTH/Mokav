def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].split())
	(n1, m1, n2, m2) = ((n - 1), m, n, (m - 1))
	(s1, s2) = ('R', 'B')
	turn = 2
	for i in range(((n + m) - 1)):
	    if (turn == 1):
	        if ((s1[(- 1)] == 'R') and (n1 >= 1)):
	            n1 -= 1
	            s1 += 'R'
	        elif (m1 >= 1):
	            m1 -= 1
	            s1 += 'B'
	        else:
	            n1 -= 1
	            s1 += 'R'
	        if ((s2[(- 1)] == 'R') and (n2 >= 1)):
	            n2 -= 1
	            s2 += 'R'
	        elif (m2 >= 1):
	            m2 -= 1
	            s2 += 'B'
	        else:
	            n2 -= 1
	            s2 += 'R'
	    else:
	        if ((s1[(- 1)] == 'R') and (m1 >= 1)):
	            m1 -= 1
	            s1 += 'B'
	        elif (n1 >= 1):
	            n1 -= 1
	            s1 += 'R'
	        else:
	            m1 -= 1
	            s1 += 'B'
	        if ((s2[(- 1)] == 'R') and (m2 >= 1)):
	            m2 -= 1
	            s2 += 'B'
	        elif (n2 >= 1):
	            n2 -= 1
	            s2 += 'R'
	        else:
	            m2 -= 1
	            s2 += 'B'
	    turn = (3 - turn)
	ans1 = sum([1 for i in range(((n + m) - 1)) if (s1[i] == s1[(i + 1)])])
	ans2 = sum([1 for i in range(((n + m) - 1)) if (s2[i] == s2[(i + 1)])])
	ans = max(ans1, ans2)
	ret_values.append(ans, (((n + m) - 1) - ans))

	return ret_values
