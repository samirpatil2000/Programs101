from importlib_metadata import version


class Solution:
    def get_int(self, version_):
        version_ = [int(s) for s in version_.split(".")]
        i = len(version_) - 1
        while i >= 0 and version_[i] == 0:
            version_.pop()
            i -= 1
        return version_
        
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = self.get_int(version1)
        version2 = self.get_int(version2)
        if version1 > version2:
            return 1
        elif version2 > version1:
            return -1
        return 0 
        
sol = Solution()
version1 = "1.01"
version2 = "1.001"
# version1 = "1.0"
# version2 = "1.0.0"
version1 = "0.1"
version2 = "1.1"
print(sol.compareVersion(version1, version2))
            