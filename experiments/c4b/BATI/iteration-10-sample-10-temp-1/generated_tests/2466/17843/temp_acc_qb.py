def patched_func(*args):
	global_list = []
	
	
	def main():
	    path = args[0]
	    if isValid(path):
	        global_list.append('OK')
	    else:
	        global_list.append('BUG')
	
	def isValid(s):
	    positions = set()
	    prev = None
	    current = (0, 0)
	    positions.add(current)
	    for c in s:
	        if (c == 'L'):
	            next = left(current)
	        elif (c == 'R'):
	            next = right(current)
	        elif (c == 'U'):
	            next = up(current)
	        elif (c == 'D'):
	            next = down(current)
	        else:
	            assert False
	        if (next == prev):
	            return False
	        prev = current
	        current = next
	        positions.add(current)
	        count = 0
	        if (left(current) in positions):
	            count += 1
	        if (right(current) in positions):
	            count += 1
	        if (up(current) in positions):
	            count += 1
	        if (down(current) in positions):
	            count += 1
	        if (count > 1):
	            return False
	    return True
	
	def left(point):
	    return ((point[0] - 1), point[1])
	
	def right(point):
	    return ((point[0] + 1), point[1])
	
	def up(point):
	    return (point[0], (point[1] + 1))
	
	def down(point):
	    return (point[0], (point[1] - 1))
	main()
	return global_list