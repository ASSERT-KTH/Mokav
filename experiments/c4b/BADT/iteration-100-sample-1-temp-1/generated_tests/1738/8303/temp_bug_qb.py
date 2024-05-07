def original_func(*args):
	global_list = []
	
	(x, y, z) = map(int, args[0].split())
	ab = set()
	ac = set()
	bc = set()
	for e in range(1, 10001):
	    if ((((x + y) % e) == 0) and ((x % e) == 0) and ((y % e) == 0)):
	        ab.add((e + ((x + y) // e)))
	    if ((((z + y) % e) == 0) and ((z % e) == 0) and ((y % e) == 0)):
	        ac.add((e + ((z + y) // e)))
	    if ((((x + z) % e) == 0) and ((x % e) == 0) and ((z % e) == 0)):
	        bc.add((e + ((x + z) // e)))
	    if ((e > (x + y)) and (e > (y + z)) and (e > (x + z))):
	        break
	global_list.append((4 * tuple(((ab & ac) & bc))[0]))
	return global_list