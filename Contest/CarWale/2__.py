import heapq
def get_maximum_beauty(k, arr):
    max_ = - 2**32
    current_sum = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        max_ = max(current_sum, max_ )
        if current_sum < 0:
            current_sum = 0
    