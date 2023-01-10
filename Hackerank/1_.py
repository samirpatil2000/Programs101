def fileProtection(fileSize, minSize):
    # count = 0
    # for i in range(len(fileSize)):
    #     if fileSize[i] < minSize[i]:
    #         count += 1
    #     elif fileSize[i] > minSize[i]:
    #         count -= fileSize[i] - minSize[i]
    # return count if count >= 0 else -1

    # function protectFiles(fileSize, minSize):
    # sort fileSize and minSize in non-ascending order of fileSize
    sorted(fileSize, minSize)

    # number of file changes we need to make
    changes = 0

    # iterate through the sorted arrays
    for i in range(0, n-1):
        # if the file is already big enough, continue
        if fileSize[i] >= minSize[i]:
            continue
        # try to transfer data from larger files to the current one
        for j in  range(i+1, n-1):
            # if the larger file can't provide enough data, continue
            if fileSize[j] < minSize[i] - fileSize[i]:
                continue
            # transfer data from the larger file to the current one
            fileSize[j] -= minSize[i] - fileSize[i]
            fileSize[i] = minSize[i]
            #  the number of changes
            changes += 1
            break
        # if we couldn't find a file that can provide enough data, return -1
        if fileSize[i] < minSize[i]:
            return -1

    # return the number of changes we made
    return changes


n = 5 
fileSize = [4, 1, 5, 2, 3]
minSize = [3, 2, 2, 1, 4]

arr = sorted(zip(fileSize, minSize), key= lambda x:( x[0], x[1]))
# print(sorted(fileSize, minSize))

print(arr)
n=5
reward_1=[5,4,3,2,1]
reward_2=[1,2,3,4,5]
k = 3
def maxReward(n, reward_1, reward_2, k):
    tasks = [(reward_1[i] - reward_2[i], i) for i in range(n)]
    tasks.sort(reverse=True)
    total_reward = 0
    for i in range(n):
        if i <= k:
            total_reward += reward_1[tasks[i][1]]
        else:
            total_reward += reward_2[tasks[i][1]]
    return total_reward
print(maxReward(n, reward_1, reward_2, k))
# print(fileProtection(fileSize, minSize))