def func(*args):
	ret_values = []
	
	R = (0, 1, 2)
	S = ['first', 'second']
	C = str.count
	s = [args[0] for _ in '123']
	v = [[] for _ in ('0' * 8)]
	for i in R:
	    for j in R:
	        v[j] += s[j][i]
	        v[(j + 3)] += s[i][j]
	    v[6] += s[i][i]
	    v[7] += s[(2 - i)][i]
	a = b = 0
	for x in v:
	    p = set(x)
	    if (p == set('X')):
	        a += 1
	    if (p == set('0')):
	        b += 1
	s = ''.join(s)
	O = C(s, '0')
	X = C(s, 'X')
	if ((O > X) or (X > (O + 1)) or (a * b) or (b and (X > O)) or (a and (X == O))):
	    r = 'illegal'
	elif ((a + b) > 0):
	    r = (('the ' + S[b]) + ' player won')
	elif (C(s, '.') == 0):
	    r = 'draw'
	else:
	    r = S[(X > O)]
	ret_values.append(r)

	return ret_values
