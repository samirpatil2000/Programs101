
# Python Implementation
 
# Locking function
def lock(name):
    ind = nodes.index(name)+1
    c1 = ind * 2
    c2 = ind * 2 + 1
    print(status)
    if status[name] == 'lock' \
            or status[name] == 'fail':
        return 'false'
    else:
        p = ind // 2
        status[nodes[p-1]] = 'fail'
        status[name] = 'lock'
        return 'true'
 
# Unlocking function
def unlock(name):
    if status[name] == 'lock':
        status[name] = 'unlock'
        return 'true'
    else:
        return 'false'
 
# Upgrade function
def upgrade(name):
    ind = nodes.index(name)+1
 
    # left child of ind
    c1 = ind * 2
 
    # right child of ind
    c2 = ind * 2 + 1
    if c1 in range(1, n) and c2 in range(1, n):
        if status[nodes[c1-1]] == 'lock' \
            and status[nodes[c2-1]] == 'lock':
            status[nodes[c1-1]] = 'unlock'
            status[nodes[c2-1]] = 'unlock'
            status[nodes[ind-1]] = 'lock'
            return 'true'
        else:
            return 'false'
 
# Precomputation
def precompute(queries):
  d = []
   
  # Traversing the queries
  for j in queries:
      i = j.split()
      d.append(i[1])
      d.append(int(i[0]))
 
  status = {}
  for j in range(0, len(d)-1, 2):
      status[d[j]] = 0
  return status, d
 
# Function to perform operations
def operation(name, code):
    result = 'false'
     
    # Choose operation to perform
    if code == 1:
        result = lock(name)
    elif code == 2:
        result = unlock(name)
    elif code == 3:
        result = upgrade(name)
    return result
   
   
# Driver Code
if __name__ == '__main__':
   
      # Given Input
    n = 7
    m = 2
    apis = 5
    nodes = ['World', 'Asia', \
            'Africa', 'China', \
            'India', 'SouthAfrica', 'Egypt']
    queries = ['1 China 9', '1 India 9', \
             '3 Asia 9', '2 India 9', '2 Asia 9']
     
    # Precomputation
    status, d = precompute(queries)
    
    print(status, d)
 
    # Function Call
    result = []
    for j in range(0, len(d) - 1, 2):
        result.append(operation(d[j], d[j + 1]))
    print(result)