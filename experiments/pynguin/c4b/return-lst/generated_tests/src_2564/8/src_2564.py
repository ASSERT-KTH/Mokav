def func(*args):
	ret_values = []
	
	
	def check_tri(Ln):
	
	    def Con(a, b, c):
	        if (((a + b) > c) and ((a + c) > b) and ((b + c) > a)):
	            return True
	        else:
	            return False
	    Con1 = (Con(Ln[0], Ln[1], Ln[2]) or Con(Ln[0], Ln[1], Ln[3]))
	    Con2 = (Con(Ln[0], Ln[2], Ln[3]) or Con(Ln[1], Ln[2], Ln[3]))
	    if (Con1 or Con2):
	        return True
	    return False
	
	def check_ln(Ln):
	    Con1 = (((Ln[0] + Ln[1]) == Ln[2]) or ((Ln[1] + Ln[2]) == Ln[3]) or ((Ln[2] + Ln[3]) == Ln[0]))
	    Con2 = (((Ln[0] + Ln[1]) == Ln[3]) or ((Ln[1] + Ln[2]) == Ln[0]) or ((Ln[2] + Ln[3]) == Ln[1]))
	    Con3 = (((Ln[0] + Ln[2]) == Ln[1]) or ((Ln[1] + Ln[3]) == Ln[2]) or ((Ln[3] + Ln[0]) == Ln[2]))
	    Con4 = (((Ln[0] + Ln[2]) == Ln[3]) or ((Ln[1] + Ln[3]) == Ln[0]) or ((Ln[3] + Ln[0]) == Ln[1]))
	    if (Con1 or Con2 or Con3 or Con4):
	        return True
	    else:
	        return False
	
	def main():
	    Line = args[0]
	    Line = Line.split()
	    for i in range(len(Line)):
	        Line[i] = eval(Line[i])
	    for i in Line:
	        if ((len(Line) != 4) or (type(i) != int) or (i <= 0) or (i > 100)):
	            ret_values.append('Enter exactly 4 positive integers lesser than 100!')
	            main()
	    if check_tri(Line):
	        ret_values.append('TRIANGLE')
	    elif check_ln(Line):
	        ret_values.append('SEGMENT')
	    else:
	        ret_values.append('IMPOSSIBLE')
	main()

	return ret_values
