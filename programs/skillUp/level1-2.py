#greedy algorithm

def solution(n, lost, reserve):
    h_reserve = set(reserve) - set(lost)
    h_lost = set(lost) - set(reserve)

    for i in h_reserve:
        if i-1 in h_reserve :
            h_lost.remove(i-1)
        elif i+1 in h_lost:
            h_lost.remove(i+1)
    answer = n-len(h_lost)
    return answer