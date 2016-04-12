




def Split(list,value):
	first = 0
	last = len(list)-1
	mid	= (first + last) / 2
	check(first,last,mid,list,value)

def check(first,last,mid,list,value):

	# print "value you searched for is ",value
	
		if list[mid]==value:
			print "Item Found !!!"
		elif value > list[mid]:
			first=mid
			mid= (first + last ) / 2
			check(first,last,mid,list,value)
		elif value < list[mid]:
			last= mid
			mid= (first + last ) / 2
			check(first,last,mid,list,value)
	
		
def main():
	# Creating the array
	list=[]
	print "Enter the elements in the lits :"
	for i in range(0,5):
		inputValue=input("")
		list.append(inputValue)
	print "your list is :",list
	value=input("Enter the value you want to search ?")
	Split(list,value)


if __name__=="__main__":
	main()


	
	