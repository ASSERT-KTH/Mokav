def func(*args):
	
	from sys import stdin, stdout
	
	def read_input():
	    inp = []
	    for line in stdin:
	        inp.append(line.strip())
	        if (line == '\n'):
	            break
	    return inp[1]
	
	def decodeSeries(chars):
	    count = 0
	    ans = ''
	    for char in chars:
	        if (char == '1'):
	            count += 1
	        else:
	            ans += str(count)
	            count = 0
	    ans += str(count)
	    return ans
	series = read_input()
	return(decodeSeries(series))
