# 작성 날짜 : 20201116
# 작성자 : 유 승 민
# 문제 명 : 나이 순 정렬
# 문제 유형: 정렬
"""
- 풀이 1 

가입 사람들의 데이터를 해쉬로 저장

키는 이름, 값은 나이,가입순서
"""

def solution():
    n = int(input())
    memberHash = {}

    for i in range(n):
        # 가입 정보를 해쉬로 저장
        member = list(input().split(" "))
        memberHash[ member[1] ] = [ int(member[0]), i ]

    ls = sorted(memberHash.items(), key=lambda x: x[1][0], reversed=True)
    print(ls)

    sameLs = []
    for i in range(n):
        # 값이 같은 구간의 시작을 구분하기 위해 len(sameLs) == 0 조건도 넣는다.
        if (ls[i] == ls[i+1]):
            # sameLs에 이름과 가입순서를 리스트로 추가한다.
            sameLs.append( [ls[i], hash[ls[i]][1] )
        if (ls[i] != ls[i+1] && len(sameLs) != 0):
            
            sameLs = []

solution()
    