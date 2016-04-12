
def searching(first,mid,last,value):
	if value == list[mid]:
		print "Item found !!!"
	elif value > list[mid]:
		first= list[mid]
		last = last
		mid = (first + last) / 2
		searching(first,mid,last,value)
	elif value < list[mid]:

		last = list[mid]
		first = first
		mid= (first + last) / 2
		searching(first,mid,last,value)
		


if __name__=="__main__":
	list=[]
	print "Enter the values to the list: "
	for i in range(0,5):
		list.append(input())

	print "The list is : ",list

 	first = 0
	last = len(list)-1
	mid	= (first + last) / 2
	value=input("Enter the value you want to search ?")
	searching(first,mid,last,value)
	
