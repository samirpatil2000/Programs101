class Solution:
    
    
    def fun(self, s):
        result = 0
        map={
            "a":1,
            "b":1,
            "c":2,
            "d":2,
            "e":2,
            "f":3,
            "g":3,
            "h":3,
            "i":4,
            "j":4,
            "k":4,
            "l":5,
            "m":5,
            "n":5,
            "o":6,
            "p":6,
            "q":6,
            "r":7,
            "s":7,
            "t":7,
            "u":8,
            "v":8,
            "w":8,
            "x":9,
            "y":9,
            "z":9
        }
        for i in range(len(s)):
            for j in range(i, len(s)):
                str_ = s[i:j + 1]
                sum_ = 0
                print(str_)
                for k in range(len(str_)):
                    sum_ += map[str_[k]]
                if sum_ % len(str_) == 0:
                    result += 1
        return result
                    
        
print(Solution().fun("bdh"))