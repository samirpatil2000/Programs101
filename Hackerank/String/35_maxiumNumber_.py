def maxNumber(operations):
    max_stack=[]
    for op in operations:
        if len(op)>1:
            if len(max_stack)==0:
                max_stack.append(int(op[2:]))
            else:
                if int(op[2:])>max_stack[len(max_stack)-1]:
                    max_stack.append(int(op[2:]))
                else:
                    max_stack.append(int(max_stack[len(max_stack)-1]))
        else:
            if int(op)==2:
                max_stack.pop()
            else:
                print(max_stack[len(max_stack)-1])
    
# maxNumber(operations)



n = int(input().strip())

ops = []

for _ in range(n):
    ops_item = input()
    ops.append(ops_item)

res = maxNumber(ops)

    
    