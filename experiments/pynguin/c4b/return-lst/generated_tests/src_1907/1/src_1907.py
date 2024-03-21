def func(*args):
	ret_values = []
	
	chess = [args[0] for i in range(8)]
	solve = 'YES'
	for c in chess:
	    if (('WW' in c) or ('BB' in c)):
	        solve = 'NO'
	        break
	    else:
	        continue
	ret_values.append(solve)

	return ret_values
