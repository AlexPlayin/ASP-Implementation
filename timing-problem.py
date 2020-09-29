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



def calc_memo():
    # Generate Table
    table = {}
    queue = []

    for i in range(0, len(start_times)):
        for j in range(i, len(start_times)):
            queue.append((i,j))
    queue.sort(key=lambda tup: tup[1] - tup[0])

    print("QueueSize", len(queue))

    for i in range(0, len(queue)):
        entry = queue[i]
        S = calc_s(entry[0], entry[1])

        if S == []:
            table[entry] = 0

        calcs = [0]

        for index,k in enumerate(S):
            calcs.append(table[(entry[0],k)] + table[(k,entry[1])] + 1)  
        
        table[entry] = max(calcs)
        #queue.remove(entry)
        #print(queue)

    return table[(0,len(start_times)-1)]

def calc_greedy():
    n = len(start_times_greedy)
    A = [1]
    k = 1
    for m in range(2,n):
        if start_times_greedy[m] >= end_times_greedy[k]:
            A.append(m)
            k = m
    return len(A)


def generate_activities(n):
    import random
    import math

    global start_times, end_times, start_times_greedy, end_times_greedy


    start_times = [-1]
    end_times = [0]

    values = []

    for i in range(0, n):

        s = math.floor(random.uniform(0, 24))
        e = math.floor(random.uniform(1, 12)) + s

        if e > 24:
            e = 24

        values.append((s,e))

    values.sort(key=lambda tup: tup[1])
    
    for i in values:
        start_times.append(i[0])
        end_times.append(i[1])

    start_times.append(24)
    end_times.append(25)

    start_times_greedy = start_times[:-1]
    end_times_greedy = end_times[:-1]


# execution
import time

generate_activities(60)

amount = 1


times = {
    "rec": 0,
    "dyn": 0,
    "greedy":0
}
for i in range(0,amount):
    print(f"\r {i}/{amount}", end="")
    memo = {}
    timer1 = time.time()
    calc_recursive(0, len(start_times) - 1)
    times["rec"] += time.time() - timer1
    
    timer1 = time.time()

    calc_memo()
    times["dyn"] += time.time() - timer1

    timer1 = time.time()
    calc_greedy()
    times["greedy"] += time.time() - timer1

for i in times:
    print(i, times[i] / amount, "s")
