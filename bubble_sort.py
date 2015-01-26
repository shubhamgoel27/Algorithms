def bubble_sort(list1):
	length = len(list1)
	for i in range(length):
		for j in range(1,length):
			if list1[j]<list1[j-1]:
				list1[j],list1[j-1] = list1[j-1], list1[j]
	print list1
	return list1
	
def main():
	bubble_sort([5,4,10,5,20,64,1,7,2,75,65,44,666,1,2,55,43,2,7,9,5])

if __name__ =='__main__':	
	main()
