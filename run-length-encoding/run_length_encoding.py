def decode(string):
	"""
	set two strings to empty, one for a character count 
	integer, the other for characters
	"""
	result = ''
	count = ''
	"""
	loop through string, if loop iteration is a digit, then
	add char to count string
	"""
	for char in string:
		if char.isdigit():
			count += char
		else:
			"""
			build result string, if count is populated,
			there will be an int here as char count. If not,
			then add the single character
			"""
			if count:
				result += int(count) * char
			else:
				result += char
			# set count back to empty
			count = ''
	return result


def encode(string):
	# check if string is empty, if evaluates to False, return empty string
	if string:
		"""
		define instance character, starting at index 0
		initialize counter var
		initialize result variable as empty string
		"""
		current_char = string[0]
		count = 0
		result = ''
		"""
		looping through string, increment counter variable
		if same character is found
		"""
		for char in string:
			if current_char == char:
				count += 1
			else:
				"""
				if count still == 1, return character for result
				else, return count of character followed by character
				"""
				if count == 1:
					result += current_char
				else:
					result += str(count) + current_char
				# set current_char to current iteration and counter back to 1
				current_char = char
				count = 1
		# still need last iteration
		if count == 1:
			result += current_char
		else:
			result += str(count) + current_char
		return result
	else:
		return ''



print(decode('5ABT3G'))
print(encode('AAAAABTGGG'))