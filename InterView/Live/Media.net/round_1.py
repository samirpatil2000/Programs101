"""
0, 1, 2,
[2,2,-1,1,1,5] - will reach the last index
[1,-1,0,1,1,4,6] - will be stuck in a loop
Count = len(arr)
"""
class Solution:
	def jump_last_index(self, arr):
		jump_count = len(arr)
        index_ = 0
		while jump_count:
            index_ += arr[index_]
            if index_ < 0 or index_ >= len(arr):
                return False
            # 2 = arr[0 + 2]
            jump_count -= 1
            if index_ == len(arr) - 1:
                return True
        return False




"""
# Q2- Given a singly linked list of characters, write a function that returns true if the given list is a palindrome, else false.

[ 1, 2, 3, 2, 1]
1 -> 2 -> 3 -> 2 -> 1 # 5/2 --> 2
# time : O(n) + O(n) ~ O(n)
# space O(n/2) ~ o(n)
# 
"""


st = [ ] 


class Solution:
    def find_len_ll(self, head):
        len_ = 0
        while head:
            head = head.next
            len_ += 1
        return len_
    def is_palindrome_ll(self, head: "Node"):
        actual_len = self.find_len_ll(head)
        len_of_ll =  actual_len // 2
        root = head
        while root and len_of_ll:
            st.append(root.val)
            root = root.next
            len_of_ll -= 1
        if actual_len & 1 == 1: # checking it is odd or not
            root = root.next
        while st:
            if root.val != st.pop():
                return False
            root = root.next
        return True
    def make_arr(self, head:"Node"):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr
            
    def is_palindrome_ll_2(self, head:"Node"):
        arr = self.make_arr(head)
        for i in range(len(arr) // 2):
            if arr[i] != arr[len(arr) - 1 - i]:
                return False
        return True



"""
Q3 - Given an integer array A, find the subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.
Example 1:
Input: nums = [-2, 1, -3, 4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

"""
nums = [-2, 1, -3, 4,-1,2,1,-5,4]

result = -2
current_sum = -2
class Solution:

    def subarray_sum(self, arr):
        current_sum = arr[0]
        result = arr[0]
        for i in range(1, len(arr)):
            if current_sum < 0:
                current_sum = 0
            current_sum += arr[i]
            result = max(current_sum, result)
        return result



nums= [-3, -5]

current_sum = -3, 0, -5
result = -3, -3 