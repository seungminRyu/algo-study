def solution(clothes):
    clothHash = {}
    answer = 1
    
    for set in clothes:
        clothType = set[1]
        if(clothType in clothHash):
            clothHash[clothType] += 1
        else:
            clothHash[clothType] = 2
    
    typeNum = list(clothHash.values())

    for i in typeNum:
        answer *= i
    answer -= 1

    print(answer)
    
testcase1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
testcase2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

solution(testcase1)
solution(testcase2)