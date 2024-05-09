def original_func(*args):
	global_list = []
	
	abStone = args[0].split()
	for i in range(len(abStone)):
	    abStone[i] = int(abStone[i])
	loop = True
	
	def gcd(x, y):
	    while (y != 0):
	        (x, y) = (y, (x % y))
	    return x
	counter = 0
	while loop:
	    gcf = gcd(abStone[0], abStone[2])
	    abStone[2] -= gcf
	    if (abStone[2] < 0):
	        loop = False
	        break
	    else:
	        counter += 1
	    gcf = gcd(abStone[0], abStone[2])
	    abStone[2] -= gcf
	    if (abStone[2] < 0):
	        loop = False
	        break
	    else:
	        counter += 1
	if ((counter % 2) == 1):
	    global_list.append('0')
	else:
	    global_list.append('1')
	return global_list