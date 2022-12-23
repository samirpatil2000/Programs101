from typing import List


class Solution:
    
    def merge(self,arr:List[int],left:int,mid:int,right:int):
        i = left
        j = mid + 1
        temp = []
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= right:
            temp.append(arr[j])
            j += 1
        for j,i in enumerate(range(left,right+1)):
            arr[i] = temp[j]

        
    def mergeSort(self,arr:List[int],left:int,right:int):
        if left<right:
            mid=(left+right)//2
            self.mergeSort(arr,left,mid)
            self.mergeSort(arr,mid+1,right)
            self.merge(arr,left,mid,right)
            

sol=Solution()
arr=[-1,-2,3]
print(sol.mergeSort(arr,0,len(arr)-1))
print(arr)


A = [5, 10, 16, 25]
B = [1, 8, 15, 20]


"""
Sorted arrays

Minimize |a-b| 
a E A
b E B


A = [5, 10, 11,12,13,14,15, 16, 25]
B = [1, 8, 15]


Def min_diff(A, B):
      I = 0
      J = 0
      Result = 2 ** 32
      While i < len(A) and j < len(B):
             Result = min(result, abs(A[i] - B[j]))
	If result == 0: return 0
             If A[i] > B[j]:
                 J += 1
             Else:
                  I += 1
      Return result

Tables: MySQL
Product
Buyer
Order  - user_id,, order_id
Order_item - order_id, product_id, timestamp
Address ( Foreinkey(Buyer)) - ( SHipping/Billing)


Top 5 user names who have placed maximum items in last 1 month
Order
32432 | 27


Order items
Order_id | product_id  | ts
27 | SDRE | ts
27 | WRTERER | ts
X1 —---
X2 —-------
X3 —---





Using Join:

Select O.user_id from Order as O Inner Join OrderItem as OI where O.order_id = OI.order_id group by Having



Select O.user_id , (select count(*)  from order_item where order_id = O.order_id and ts>””) as orders from Order as O asc  orders limit 5;

https://docs.google.com/document/d/12upOlZ1yenPkhrLWKoRLWDOc2SjFGXYsNKFgn5ucaNM/edit
"""