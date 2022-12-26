
# def fun(k):
    # len_s=len(s)
    # arr=[0]*len_s
    # for i in range(len_s):
    #     arr[i]=ord(s[i])-ord("a")
    # len_e=len(e)
    # i=0
    # result=""
    # while i<len_e:
    #     result+=chr(((ord(e[i])+arr[i%len_s])-ord("a"))%26+ord("a"))
    #     i+=1
    # return result
    # int n=k.length;
    #     long[] ls=new long[n];
    #     for(int i=0;i<n;i++){
    #         for(int j=1;j<k[i];j++){
    #             if(k[i]%j==0){
    #                 ls[i]+=j;
    #                 //ls[i]+=k[i]/j;
                    
    #             }
                
    #         }
    #         ls[i]+=k[i];
    #     }
    #     return ls;
    # n = len(k)
    # result = [0]*n
    # for i in range(n):
    #     for j in range(1, k[i]):
    #         if k[i]%j == 0:
    #             result[i] += j
    #     result[i] += k[i]
    # return result


x=[2,3,7]
y=[4,-6,8]

def get_area(x,y):
    area_of_trangle = abs(0.5 * ( (x[0]*(y[1]-y[2])) + (x[1]*(y[2]-y[0])) + (x[2]*(y[0]-y[1]))))
    return int(area_of_trangle)


        
# x=[0,4,7]
y=[0,8, 6]
# print(get_area(x, y))

se = set(y)
se.remove(0)
print(se)
print("ss".split())


# def MatrixChallenge(strArr):

#   # code goes here
#   return strArr

class Solution:

  def is_valid(self, matrix, row, col):
    if row < 0 or col < 0:
      return False
    if row >= len(matrix) or col >= len(matrix[0]):
      return False
    if matrix[row][col] == "#":
      return False

    return True


  def dfs(self, matrix, row, col, word, index):
    if matrix[row][col] != word[index]:
      return False
    if len(word) - 1 == index:
      return True
    temp = matrix[row][col]
    matrix[row][col] = "#"
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for i in range(8):
      new_row, new_col = row + dirs[i][0], col + dirs[i][1]
      if self.is_valid(matrix, new_row, new_col):
        if self.dfs(matrix, new_row, new_col, word, index + 1):
          return True
    matrix[row][col] = temp
    return False

  def matrix_challenge(self, string_array):
    matrix = [list(word) for word in string_array[0].split(", ")]
    print(matrix)
    result = []
    for word in string_array[1].split(","):
      if not self.find_word(matrix, word):
        result.append(word)
    if not result:
      return "true"
    ans = result[0]
    for i in range(1, len(result)):
      ans += ","
      ans += result[i]
    return ans

  def find_word(self, matrix, word):
    for row in range(len(matrix)):
      for col in range(len(matrix[0])):
        if self.dfs(matrix, row, col, word, 0):
          return True
    return False
          


# keep this function call here 


Input= ["aaey, rrum, tgmn, ball", "all,ball,mur,raeymnl,tall,true,trum"]
Input= ["aaey, rrum, tgmn, ball", "all,ball,mur,raeymnl,rumk,tall,true,trum,yes"]
Output= "rumk,yes"

print(Solution().matrix_challenge(Input))






Input= ["aaey, rrum, tgmn, ball", "all,ball,mur,raeymnl,tall,true,trum"]
Output= "true"

Input= ["aaey, rrum, tgmn, ball", "all,ball,mur,raeymnl,rumk,tall,true,trum,yes"]
Output= "rumk,yes"


