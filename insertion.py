
def insertionSort():
	list=[];
	for value in xrange(1,10):
		list.append(input());
	print "Your array is :",list

	for index in range(1,len(list)):
		currentvalue= list[index]
		position = index

		while currentvalue < list[position -1 ] and position > 0:
			list[position]= list[position - 1]
			position = position -1	
			
		list[position]=currentvalue
		print "The given list is sorted as: ",list

	print ""
	print "The sorted list is given as",list
insertionSort()