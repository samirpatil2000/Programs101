

class Solution:
    def get_max(self, arr, indx):
        if indx < 0:
            return float('-inf')
        return arr[indx]
    
    def get_min(self, arr, indx):
        if indx == len(arr):
            return float('inf')
        return arr[indx]
    
    def find_median(self, arr1, arr2, low, high):
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        x = len(arr1)
        y = len(arr2)

        low = 0
        high = x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxLeftX = float('-inf') if partitionX == 0 else arr1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else arr1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else arr2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else arr2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
                
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1

        # If the input arrays are not sorted, return -1 (invalid input)
        return -1
        
        
    def median_of_array(self, array1, array2):
        return self.find_median(array1, array2, 0, len(array1))
        
        
a1,a2  = [1,5,9], [2,3,6,7]
a1,a2  = [4,6], [1,2,3,5]
print(Solution().median_of_array(a1, a2))