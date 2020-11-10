def solution(participant, completion):
    compLs = {} #completion을 담을 딕셔너리
    answer = ""
    
    for player in completion:
        if(player in compLs):
            compLs[player] += 1
        else:
            compLs[player] = 1
            
    for player in participant:
        if(player in compLs):
            compLs[player] -= 1;
        else:
            answer = player
            return answer
    
    for player in compLs.keys():
        if (compLs[player] < 0):
            answer = player
    
    return answer

participant = ["mislav", "stanko", "mislav", "ana"]
complement = ["stanko", "ana", "mislav"]

solution(participant, complement)