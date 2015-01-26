def longest_in_order(string_to_search):
	'''Returns the longest sequence which is in alphabetical order in the string'''

	s = string_to_search
	word_list = []
	for i in range(len(s)-1):
		longest = s[i]
		j=i
		while s[j+1] >= s[j] and j<(len(s)-2):  #if next char is bigger than current
			longest = longest + s[j+1]   #append it to longest
			j+=1
			if j==len(s)-2 and ord(s[-1]) >= ord(longest[-1]): #caters to the case when the last char is bigger than previous
				longest += s[-1]
		word_list.append(longest)  
		i+=1
		#print longest

	return max(word_list,key=len)  #get the longest phrase in alphabetical order
