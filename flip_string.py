
def flip_string(string):
	string_list = list(string)
	for i in range(len(string_list)/2):
		j = len(string_list)-i-1
		first = string_list[i]
		last = string_list[j]
		string_list[i] = last
		string_list[j] = first
	reversed_string = "".join(string_list)
	return reversed_string

print flip_string('dogs and cat')
