def func(*args):
	ret_values = []
	
	"\n' Author:   Cheng-Shih Wong\n' Email:    mob5566@gmail.com\n' Date:     2017-08-07\n"
	
	def main():
	    walk = {'L': (0, (- 1)), 'U': ((- 1), 0), 'R': (0, (+ 1)), 'D': ((+ 1), 0)}
	    back = {'L': 'R', 'R': 'L', 'U': 'D', 'D': 'U'}
	
	    def update(pos, d):
	        return ((pos[0] + walk[d][0]), (pos[1] + walk[d][1]))
	
	    def check(path):
	        vis = set()
	        pos = (0, 0)
	        vis.add(pos)
	        for c in path:
	            pos = update(pos, c)
	            if (pos in vis):
	                return False
	            for nei in 'LURD':
	                if ((nei != back[c]) and (update(pos, nei) in vis)):
	                    return False
	            vis.add(pos)
	        return True
	    path = args[0]
	    ret_values.append(('OK' if check(path) else 'BUG'))
	if (__name__ == '__main__'):
	    main()

	return ret_values
