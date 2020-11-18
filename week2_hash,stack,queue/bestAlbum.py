# 작성 날짜 : 20201112
# 작성자 : 유 승 민
# 문제 명 : 베스트 엘범
# 문제 유형: hash
# 문제 요약 : 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인가? 

# 풀이 1 
# 2중 for문을 사용해서 처음부터 하나씩 비교했다.
# 시간 복잡도 :  O(N^(3/2)) 
#
# 풀이 2 
# stack 사용하면 시간복잡도가 O(N)이 나올 것이다.

def solution(genres, plays):
    songHash = {}
    songNum = len(genres)
    
    # 장르를 키로 저장 키 안에는 고유번호와 재생 횟수를 해쉬로 만들어 리스트로 넣는다.
    for genre, play, i in zip(genres, plays, range(songNum)):
        if(not(genre in songHash)):
            songHash[genre] = []            
        songHash[genre].append({ i: play })

    # 장르에서 두개를 뽑아서 리스트에 넣는다
    keys = songHash.keys()
    for k in keys:
        

testGenres = ["classic", "pop", "classic", "classic", "pop"]
testPlays = [500, 600, 150, 800, 2500]

solution(testGenres, testPlays)