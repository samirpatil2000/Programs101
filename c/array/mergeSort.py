
def merge(arr, left, mid, right): 
	n1 = mid - left + 1
	n2 = right- mid 

	LeftArray = [0] * (n1) 
	RightArray = [0] * (n2) 

	for i in range(0 , n1): 
		LeftArray[i] = arr[left + i] 

	for j in range(0 , n2): 
		RightArray[j] = arr[mid + 1 + j]
  
	i = 0
	j = 0
	k = left	 

	while i < n1 and j < n2 : 
		if LeftArray[i] <= RightArray[j]: 
			arr[k] = LeftArray[i] 
			i += 1
		else: 
			arr[k] = RightArray[j] 
			j += 1
		k += 1
	while i < n1: 
		arr[k] = LeftArray[i] 
		i += 1
		k += 1

	while j < n2: 
		arr[k] = RightArray[j] 
		j += 1
		k += 1
 
def mergeSort(arr,left,right): 
	if left < right: 
		mid = (left+right)//2

		mergeSort(arr, left, mid) 
		mergeSort(arr, mid+1, right) 
		merge(arr, left, mid, right) 




