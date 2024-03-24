def func(*args):
	ret_values = []
	
	import sys
	
	def read():
	    global gl, gr, bl, br
	    girl = input.readline()
	    gl = int(girl.split(' ')[0])
	    gr = int(girl.split(' ')[1])
	    boy = input.readline()
	    bl = int(boy.split(' ')[0])
	    br = int(boy.split(' ')[1])
	
	def check_possible(g, b):
	    if (g == b):
	        return True
	    elif (g > b):
	        if (b == (g - 1)):
	            return True
	        else:
	            return False
	    elif (g < b):
	        if (b <= ((2 * g) + 2)):
	            return True
	        else:
	            return False
	
	def main():
	    poss = check_possible(gl, br)
	    if poss:
	        output.write('YES')
	        return
	    poss = check_possible(gr, bl)
	    if poss:
	        output.write('YES')
	        return
	    output.write('NO')
	
	def run():
	    global input, output
	    input = sys.stdin
	    output = sys.stdout
	    read()
	    main()
	if (__name__ == '__main__'):
	    run()

	return ret_values
