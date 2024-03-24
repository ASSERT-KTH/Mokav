def func(*args):
	
	__author__ = 'markdaniel'
	import math
	
	def does_fit(plates, t_radius, p_radius):
	    a = b = float((t_radius - p_radius))
	    if (a <= 0):
	        return ('YES' if ((plates == 1) and (a == 0)) else 'NO')
	    if (a < p_radius):
	        return ('YES' if (plates == 1) else 'NO')
	    c = float((2 * p_radius))
	    cosC = (float((((a * a) + (b * b)) - (c * c))) / ((2 * a) * b))
	    angleC = math.degrees(float(math.acos(cosC)))
	    angleC = round(angleC, 13)
	    return ('YES' if ((360.0 / angleC) >= plates) else 'NO')
	if (__name__ == '__main__'):
	    (plates, t_radius, p_radius) = [int(x) for x in args[0].split(' ')]
	    return(does_fit(plates, t_radius, p_radius))
