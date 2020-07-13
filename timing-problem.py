start_times = [-1,1,3,0,5,3,5, 6, 8, 8, 2,12,17]
end_times =   [0,4,5,6,7,9,9,10,11,12,14,16,18]
#               [0,1,2,3,4,5, 6, 7, 8, 9,10]
start_times_greedy = start_times[:-1]
end_times_greedy = end_times[:-1]
# Calculates S[i,j]
def calc_s(i,j):
    if i > j:
        return []
    if i == j:
        return []
    
    result = []

    for k, value in enumerate(start_times):
        if start_times[k] >= end_times[i] and end_times[k] <= start_times[j]:
            result.append(k)

    return result

def calc_recursive(i,j):
    S = calc_s(i,j)
    if S == []:
        return 0
    
    calcs = []
    for index,k in enumerate(S):
        calcs.append(calc_recursive(i,k) + calc_recursive(k,j) + 1)
    
    return max(calcs)

memo = {}

def calc_memo(i,j):
    if (i,j) in memo:
        return memo[(i,j)]
    S = calc_s(i,j)
    if S == []:
        return 0
    
    calcs = []
    for index,k in enumerate(S):
        calcs.append(calc_memo(i,k) + calc_memo(k,j) + 1)
    
    return_val = max(calcs)
    memo[(i,j)] = return_val
    return return_val

def calc_greedy():
    n = len(start_times_greedy)
    A = [1]
    k = 1
    for m in range(2,n):
        if start_times_greedy[m] >= end_times_greedy[k]:
            A.append(m)
            k = m
    return len(A)

# execution
import time

times = {
    "rec": 0,
    "memo": 0,
    "greedy":0
}

for i in range(0,1000000):
    print(f"\r {i}/1000000", end="")
    memo = {}
    timer1 = time.time()
    calc_recursive(0, len(start_times) - 1)
    times["rec"] += time.time() - timer1
    
    timer1 = time.time()
    calc_memo(0, len(start_times) - 1)
    times["memo"] += time.time() - timer1

    timer1 = time.time()
    calc_greedy()
    times["greedy"] += time.time() - timer1

for i in times:
    print(i, times[i] * 10000000 / 1000000, "us")