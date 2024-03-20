def func(*args):
	
	chess = [args[0] for i in range(8)]
	solve = 'YES'
	for c in chess:
	    if (('WW' in c) or ('BB' in c)):
	        solve = 'NO'
	        break
	    else:
	        continue
	return(solve)
