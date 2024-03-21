def func(*args):
	ret_values = []
	
	__author__ = 'artyom'
	
	def main():
	    (d1, d2, d3) = read(3)
	    return min((2 * (d1 + d2)), (2 * (d1 + d3)), (2 * (d2 + d3)), ((d1 + d2) + d3))
	
	def read(mode=1, size=None):
	    if (mode == 0):
	        return args[0].strip()
	    if (mode == 1):
	        return int(args[1].strip())
	    if (mode == 2):
	        return args[2].strip().split()
	    if (mode == 3):
	        return list(map(int, args[3].strip().split()))
	    a = []
	    for _ in range(size):
	        a.append(read(3))
	    return a
	
	def write(s='\n'):
	    if (s is None):
	        s = ''
	    if (isinstance(s, tuple) or isinstance(s, list)):
	        s = ' '.join(map(str, s))
	    s = str(s)
	    ret_values.append(s, end='\n')
	res = main()
	write(res)

	return ret_values
