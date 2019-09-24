def quickSort(array):
	if len(array) < 2:
		return array
	else:
		base = array[0]
		less = [i for i in array[1:] if i <= base]
		greater = [i for i in array[1:] if i > base]
		newArray = quickSort(less) + [base] + quickSort(greater)
		return newArray

list = [1,5,8,2,4,5,3,6]
newArray = quickSort(list)
print(newArray)