def func(*args):
	ret_values = []
	
	import copy
	
	def main():
	    lst_of_sides = [int(i) for i in args[0].split()]
	    lst_of_sides1 = copy.copy(lst_of_sides)
	    if IsTriangle(lst_of_sides):
	        ret_values.append('TRIANGLE')
	    elif IsSegment(lst_of_sides1):
	        ret_values.append('SEGMENT')
	    else:
	        ret_values.append('IMPOSSIBLE')
	
	def IsTriangle(lst):
	    istriangle = False
	    max1 = max(lst)
	    lst.remove(max1)
	    lst1 = copy.copy(lst)
	    max2 = max(lst1)
	    lst1.remove(max2)
	    if ((max1 < (lst[0] + lst[1])) or (max1 < (lst[0] + lst[2])) or (max1 < (lst[1] + lst[2]))):
	        istriangle = True
	    elif (max2 < (lst1[0] + lst1[1])):
	        istriangle = True
	    return istriangle
	
	def IsSegment(lst):
	    issegment = False
	    if ((lst[0] == (lst[1] + lst[2])) or (lst[0] == (lst[1] + lst[3])) or (lst[0] == (lst[2] + lst[3]))):
	        issegment = True
	    elif ((lst[1] == (lst[0] + lst[2])) or (lst[1] == (lst[0] + lst[3])) or (lst[1] == (lst[2] + lst[3]))):
	        issegment = True
	    elif ((lst[2] == (lst[0] + lst[1])) or (lst[2] == (lst[0] + lst[3])) or (lst[2] == (lst[1] + lst[3]))):
	        issegment = True
	    elif ((lst[3] == (lst[0] + lst[1])) or (lst[3] == (lst[0] + lst[2])) or (lst[3] == (lst[1] + lst[2]))):
	        issegment = True
	    return issegment
	main()

	return ret_values
