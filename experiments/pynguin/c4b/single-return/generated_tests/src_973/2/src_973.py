def func(*args):
	
	a_str = ['first', 'second', 'illegal', 'the first player won', 'the second player won', 'draw']
	gl = [args[0] for i in range(3)]
	(ai, n1, n2, f3, f4) = ((- 1), 0, 0, 0, 0)
	for s in gl:
	    n1 += s.count('X')
	    n2 += s.count('0')
	if ((n1 == n2) or ((n1 - n2) == 1)):
	    for i in range(3):
	        if ((gl[i][0] == gl[i][1] == gl[i][2] == 'X') or (gl[0][i] == gl[1][i] == gl[2][i] == 'X')):
	            f3 = 1
	        if ((gl[i][0] == gl[i][1] == gl[i][2] == '0') or (gl[0][i] == gl[1][i] == gl[2][i] == '0')):
	            f4 = 1
	    if ((f3 == 0) and (f4 == 0)):
	        if ((gl[0][0] == gl[1][1] == gl[2][2] == 'X') or (gl[2][0] == gl[1][1] == gl[0][2] == 'X')):
	            f3 = 1
	        if ((gl[0][0] == gl[1][1] == gl[2][2] == '0') or (gl[2][0] == gl[1][1] == gl[0][2] == '0')):
	            f4 = 1
	    if ((f3 == 1) and (f4 == 0) and ((n1 - n2) == 1)):
	        ai = 3
	    elif ((f3 == 0) and (f4 == 1) and (n1 == n2)):
	        ai = 4
	    elif ((f3 == 0) and (f4 == 0)):
	        if (n1 == n2):
	            ai = 0
	        elif ((n1 - 1) == n2):
	            ai = (5 if (n2 == 4) else 1)
	return(a_str[(ai if (ai != (- 1)) else 2)])
