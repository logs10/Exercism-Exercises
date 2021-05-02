def reverse(input=''):
	"""Reverse a given string, return empty string if empty string passed"""
	sorted_list = []
	if input:
		for index, char in enumerate(input):
			sorted_list.append(tuple([index, char]))
			sorted_list.sort(reverse=True)
			sorted2 = [char[1] for char in sorted_list]
		return ''.join(sorted2)
	else:
		return ''