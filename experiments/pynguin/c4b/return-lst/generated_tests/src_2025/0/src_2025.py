def func(*args):
	ret_values = []
	
	from collections import deque
	names = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	n_first_sheldon = []
	space_between = []
	x = (- 1)
	y = 1
	z = 5
	m = 0
	while (x < (10 ** 9)):
	    n_first_sheldon.append(y)
	    x = y
	    z = (5 * (2 ** m))
	    space_between.append(z)
	    y += z
	    m += 1
	n = int(args[0])
	queue = deque(names)
	current = None
	
	def larger(n):
	    for i in range(len(n_first_sheldon)):
	        if (n_first_sheldon[i] > n):
	            return (int((space_between[(i - 1)] / 5)), n_first_sheldon[(i - 1)], n_first_sheldon[i])
	(copies, start, nexter) = larger(n)
	hue = (n - start)
	magic = (hue // copies)
	ret_values.append(names[magic])

	return ret_values
