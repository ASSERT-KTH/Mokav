def func(*args):
	ret_values = []
	
	
	def main():
	    import sys
	    data = [line.rstrip().split() for line in sys.stdin.readlines()]
	    positions = [int(x) for x in data[0]]
	    moves = [int(x) for x in data[1]]
	    (x1, y1) = (positions[0], positions[1])
	    (x2, y2) = (positions[2], positions[3])
	    (x, y) = (moves[0], moves[1])
	    m = ((x2 - x1) / x)
	    n = ((y2 - y1) / y)
	    if (m.is_integer() and n.is_integer() and (((int(m) - int(n)) % 2) == 0)):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')
	if (__name__ == '__main__'):
	    main()

	return ret_values
