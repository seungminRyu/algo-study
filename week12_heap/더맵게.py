def mix(a1, a2):
    if a2 > a1:
        mixed = a1 + (a2 * 2)
    else:
        mixed = a2 + (a1 * 2)
    return mixed

def solution(sc, k):
    sc.sort()
    l = len(sc)
    cnt = 0

    for i in range(l):
        if sc[i] >= k:
            break
        sc[i+1] = mix(sc[i], sc[i+1])
        cnt += 1
    
    return cnt

solution(sc, k)