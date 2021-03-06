
def printMat(arr,N):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
        print()

def create(arr,N):
    # solution by samir patil
    for i in range(N):
        arr[i][i] = 1
    for i in range(N):
        arr[i][N - i - 1] = 1
    if (N % 2 != 0):
        arr[N // 2][0] = 1
        arr[0][N // 2] = 1


N=int(input("Enter the matrix"))
arr = [[0 for i in range(N)] for i in range(N)]
create(arr,N)
printMat(arr,N)