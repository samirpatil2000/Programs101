X1, Y1 = 19.021799917866176, 72.87008087597307 # centre  
X2, Y2 = 19.02142838655109, 72.87198109437252 



X1, Y1 = 19.034163663763668, 72.85948103715276 # centre  
X2, Y2 = 19.03094758899461, 72.85812531305028


import math

def get_distance(x1, y1, x2, y2):
    result = (x1 - x2)**2 + (y1 - y2)**2
    return math.sqrt(result)


print(get_distance(X1, Y1, X2, Y2) * 1e5 <= 205)

# 0.0019361987200868216
# 220meter
