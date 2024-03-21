def func(*args):
	ret_values = []
	
	'input\n!RGYB\n'
	s = args[0]
	(r, y, g, b) = [(s.index(i) % 4) for i in 'RYGB']
	(d, a, t) = ({r: 'R', y: 'Y', g: 'G', b: 'B'}, {'R': 0, 'Y': 0, 'G': 0, 'B': 0}, [])
	for x in range(len(s)):
	    if (s[x] == '!'):
	        a[d[(x % 4)]] += 1
	for y in 'RBYG':
	    ret_values.append(a[y], end=' ')

	return ret_values
