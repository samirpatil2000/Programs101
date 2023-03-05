class Solution:
    def count_set_bit(self, n):
        m = n
        if n == 0:
            return 0
        counter = 0
        while n:
            counter += (n&1)
            n >>= 1
        print(m, counter)
        return counter
    def sortBySetBitCount(self, arr, n):
        # Your code goes here
        # x = list(range(len(arr)))
        # x.sort(key=lambda i: (-self.count_set_bit(arr[i]), i))
        y = [i[1] for i in sorted(enumerate(arr), key=lambda item: (-self.count_set_bit(item[1]), item[0]))]

        return y
    
    
arr = [5, 2, 3, 9, 4, 6, 7, 15, 32]
print(Solution().sortBySetBitCount(arr, len(arr)))