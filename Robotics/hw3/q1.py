memo = {}
def cost_to_go(state):
    #if it is not in the memo table, we will get the
    #cost to go for the previous state (which should already 
    # be in the table) and add it with the new edge
    if state not in memo:
        memo[state] = cost_to_go(state[:len(state)-1]) \
            + cost_to_go(state[len(state)-2:])
    return memo[state]

#modify the edge cost for alpha and return true if
#it makes the given route a lowest cost path
def optimal_route(final_state):
    for state in states:
        cost_to_go_final_states[state] = cost_to_go(state)
    cost_final_state = cost_to_go_final_states[final_state]
    for cost in cost_to_go_final_states.values():
        if cost < cost_final_state:
            return False
    return True

#represent the graph as a 2D array edges, where
#edges[i] takes the form ['A', 'B', 2], where A and
#B are nodes and the undirected edge between them
#has a weight of 2
#reset the memo table with edge weights based on alpha
def set_memo_table(alpha):
    edges = [['A', 'B', 2], 
             ['A', 'C', 1], 
             ['A', 'D', 1],
             ['B', 'C', alpha],
             ['B', 'D', 2], 
             ['C', 'D', 2]]
    #set up a memoization dictionary where each entry will
    #represent the cost to go of a certain state
    #e.g. entry 'AB' will be 2 and 'ABD' will be 4
    memo = {}
    #add entries for all of the edges
    #add an entry for both ways to traverse the edge
    #since the graph is undirected (e.g. 'AD' == 'DA')
    for edge in edges:
        state = edge[0] + edge[1]
        altState = edge[1] + edge[0]
        memo[state] = edge[2]
        memo[altState] = edge[2]
    return memo

#compute the cost to go for each state in figure 2
cost_to_go_final_states = {}
states = ['ABCDA', 'ABDCA', 'ACBDA', 'ACDBA', 'ADBCA', 'ADCBA']
#for each final state, get the optimal interval of alpha
#as a two element array [start, finish]
#if thesre is no interval, enter the empty array []
#also cap the interval at 10 as the alpha value will not
#improve the interval after that (so the interval
# [0, 10] is equivalent to [0, infinity))
optimal_alpha_intervals = {}
for state in states:
    start = -1
    finish = -1
    alpha = 0
    while True:
        memo = set_memo_table(alpha)
        if start == -1 and optimal_route(state):
            start = alpha
        elif start != -1 and not optimal_route(state):
            finish = alpha - 1
            break
        alpha += 1
        #just cut off alpha at a point because it will not make
        #the path more optimal
        if alpha >= 10:
            finish = alpha
            break
    interval = [] if start == -1 or finish == -1 else [start, finish]
    optimal_alpha_intervals[state] = interval
print(optimal_alpha_intervals)