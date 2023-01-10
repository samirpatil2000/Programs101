class Solution:
    def totalFruit(self, tree: list) -> int:
        dict_ = {}
        start = 0
        result = 0
        for i in range(len(tree)):
            print(dict_)
            dict_[tree[i]] = dict_.get(tree[i], 0) + 1
            if len(dict_) < 3:
                result = max(result, sum(dict_.values()))
            else:
                dict_[tree[start]] -= 1
                if dict_[tree[start]] == 0:
                    del dict_[tree[start]]
                start += 1
        return result
        

arr = [0,1,1,4,3]
arr = [1,2,3,2,2]
# arr = [3,3,3,1,2,1,1,2,3,3,4]
print(Solution().totalFruit(arr))

[3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]



# {} 3 start 0 current_index 0
# {3: 1} 3 start 0 current_index 1
# {3: 2} 3 start 0 current_index 2
# {3: 3} 1 start 0 current_index 3
# {3: 3, 1: 1} 2 start 0 current_index 4
# {1: 1, 2: 1} 1 start 3 current_index 5
# {1: 2, 2: 1} 1 start 3 current_index 6
# {1: 3, 2: 1} 2 start 3 current_index 7
# {1: 3, 2: 2} 3 start 3 current_index 8
# {2: 2, 3: 1} 3 start 6 current_index 9
# {2: 2, 3: 2} 4 start 6 current_index 10




# count, i = {}, 0
# for j, v in enumerate(tree):
#     count[v] = count.get(v, 0) + 1
#     if len(count) > 2:
#         count[tree[i]] -= 1
#         if count[tree[i]] == 0: del count[tree[i]]
#         i += 1
# return j - i + 1






[3,3,3,1,2,1,1,2,3,3,4]

