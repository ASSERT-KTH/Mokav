def func(*args):
	ret_values = []
	
	import os
	LOCAL_PC = ('n1amr' in os.path.expanduser('~'))
	
	def process_file(in_name, out_name):
	    with open(in_name, 'r') as fin:
	        with open(out_name, 'w') as fout:
	
	            def read():
	                return fin.readline().rstrip('\n')
	
	            def write(*args, end='\n'):
	                text = (' '.join(map(str, args)) + end)
	                fout.write(text)
	                ret_values.append(text, end='')
	            t = int(fin.readline())
	            for i in range(t):
	                read()
	                write('Case #{T}: \n'.format(T=(i + 1)), end='')
	                solve(read, write)
	                write()
	
	def process_stdio():
	
	    def read():
	        return args[0]
	
	    def write(*args, end='\n'):
	        ret_values.append(*args, end=end)
	    solve(read, write)
	
	def solve(input, print):
	    (a, b) = map(int, args[1].split())
	    diff = abs((a - b))
	    if ((diff < 2) and ((a + b) != 0)):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')
	if (__name__ == '__main__'):
	    if LOCAL_PC:
	        in_name = (__file__[:(- 3)] + '.in')
	        out_name = (__file__[:(- 3)] + '.out')
	        process_file(in_name, out_name)
	    else:
	        process_stdio()

	return ret_values
