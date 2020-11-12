def solution(genres, plays):
    songHash = {}
    songNum = len(genres)
    
    for genre, play, i in zip(genres, plays, range(songNum)):
        if(not(genre in songHash)):
            songHash[genre] = []            
        songHash[genre].append({ i: play })
    
    print(songHash)

testGenres = ["classic", "pop", "classic", "classic", "pop"]
testPlays = [500, 600, 150, 800, 2500]

solution(testGenres, testPlays)