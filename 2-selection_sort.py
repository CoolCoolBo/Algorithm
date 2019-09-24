***********************************快速排序************************************
def find_smallest(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in range(1,len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index


def selectionSort(arr):
	newArr = []
	for i in range(len(arr)):
		smallest = find_smallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr

arr = [2,4,6,3,1,5,8,7,10]
newArr = selectionSort(arr)
print(newArr)