def patched_func(*args):
	global_list = []
	
	import math
	import re
	from fractions import Fraction
	from collections import Counter
	
	class Task():
	    (a, b) = (0, 0)
	    answer = 0
	
	    def __init__(self):
	        (self.a, self.b) = [x for x in args[0].split()]
	
	    def solve(self):
	        (a, b) = (self.a, self.b)
	        self.answer = (int(a) + int(b[::(- 1)]))
	
	    def printAnswer(self):
	        global_list.append(self.answer)
	task = Task()
	task.solve()
	task.printAnswer()
	return global_list