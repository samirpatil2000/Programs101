"""
Cargo-Dropping-Ships


There is a cargo ship that contains an unlimited amount of cargo in it. The ship is ready to sail and you have a list of N non-negative integers which denotes the water level in the sea at the ith points. A wave is defined as the continuously decreasing water level or continuously increasing water level.


Let A= [1,2,6,4,2,3,1,8,9,7], it has 6 waves in it [1,2,6],[6,4,2],[2,3],[3,1],[1,8,9],[9,7]


The amount of cargo that falls into the sea is equal to the product of the smallest height of the wave and length of the wave.

You have to find the total amount of cargo which falls into the sea.


NOTE: No two adjacent value will be equal in the list.


Input:

First-line contains T-number of TestCases. Then for every test case,

• 1st line contains a non-negative integer N.

• The next line contains a list of N space-separated integer denoting the water level at the ith point.


Output:

The total amount of cargo that falls into the sea.


Constraints:

1 <= T <= 1e3

2 <= N <= 1e5

1 <= A[i] <= 1e5


Note: The sum of N in a test would not exceed 1e10


Sample test cases:


1

10

1 2 6 4 2 3 1 8 9 7


Sample output:

32

"""

def findCargo(arr):
    map = {}
    i = 0 
    key = 0
    while i < len(arr) - 1:
        if arr[i] < arr[i + 1]:
            list_ = []
            while (i < len(arr) - 1 and arr[i] < arr[i + 1]):
                list_.append(arr[i])
                i += 1
            list_.append(arr[i])
            map[key] = list_
            key += 1
            continue
        else:
            list_ = []
            while (i < len(arr) - 1 and arr[i] > arr[i + 1]):
                list_.append(arr[i])
                i += 1
            list_.append(arr[i])
            map[key] = list_
            key += 1
            continue
        i += 1
        print(i)
    return map

arr = [1, 2, 6, 4, 2, 3, 1, 8, 9, 7]
print(findCargo(arr))