def solution(clothes):
    clothHash = {}
    
    for set in clothes:
        cloth = set[0]
        clothType = set[1]
        if(clothType in clothHash):
            clothHash[clothType].append(cloth)
        else:
            clothHash[clothType] = []
            clothHash[clothType].append(cloth)

    print(clothHash)
    
testcase1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
testcase2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

solution(testcase1)
solution(testcase2)