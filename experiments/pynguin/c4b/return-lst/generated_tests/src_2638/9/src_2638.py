def func(*args):
	ret_values = []
	
	'\n\n    Вредная Клавиатура\n\n    http://codeforces.com/problemset/problem/801/A\n\n\n\n    У Тонио есть клавиатура с двумя клавишами: буквой «V» и буквой «K».\n\n\n\n    Однажды он набрал строку s, используя только эти две буквы. Ему нравится, когда он\n\n    встречает подстроку «VK», поэтому он хочет изменить не больше одной буквы в строке\n\n    (или не изменять ничего), чтобы максимизировать число вхождений этой подстроки.\n\n    Вычислите максимальное число раз, которое строка «VK» может встретиться как\n\n    подстрока (т. е. буква «K» сразу после буквы «V») в получившейся строке.\n\n\n\n    Входные данные\n\n    Единственная строка содержит строку s, которая состоит только из заглавных букв\n\n    латинского алфавита «V» или «K» и имеет длину от 1 до 100.\n\n\n\n    Выходные данные\n\n    Выведите одно число — максимальное число раз, которое строка «VK» может встречаться\n\n    как подстрока в данной строке после изменения не более одного символа.\n\n'
	import fileinput
	
	def get_max_vk(input_string):
	    if (not isinstance(input_string, str)):
	        raise TypeError('Value should be string')
	    s_len = len(input_string)
	    if ((s_len < 1) or (s_len > 100)):
	        raise ValueError('String length should be between 1 and 100')
	    parts = input_string.split('VK')
	    total = (len(parts) - 1)
	    can_sub = False
	    for part in parts:
	        if (len(part) < 2):
	            continue
	        last_char = ''
	        for char in part:
	            if (char == last_char):
	                can_sub = True
	                break
	            last_char = char
	        if can_sub:
	            break
	    return (total + (1 if can_sub else 0))
	if (__name__ == '__main__'):
	    for line in fileinput.input():
	        ret_values.append(get_max_vk(line.rstrip('\n')))

	return ret_values
