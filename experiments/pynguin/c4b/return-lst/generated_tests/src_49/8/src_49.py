def func(*args):
	ret_values = []
	
	import sys
	input = sys.stdin.readline
	players = int(args[0])
	fib1 = 2
	fib2 = 3
	winner = 1
	while True:
	    cat = fib1
	    fib1 = fib2
	    fib2 += cat
	    if (fib1 > players):
	        ret_values.append(winner)
	        break
	    else:
	        winner += 1

	return ret_values
