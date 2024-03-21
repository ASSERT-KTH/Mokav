def func(*args):
	ret_values = []
	
	import sys
	
	def main():
	    inp = input.readline().split(' ')
	    n = int(inp[0])
	    a = int(inp[1])
	    b = int(inp[2])
	    output.write(str(((n - max((a + 1), (n - b))) + 1)))
	
	def run():
	    global input, output
	    input = sys.stdin
	    output = sys.stdout
	    main()
	if (__name__ == '__main__'):
	    run()

	return ret_values
