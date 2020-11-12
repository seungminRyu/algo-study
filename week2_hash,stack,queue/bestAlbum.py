def solution(genres, plays):
    songHash = {}
    songNum = len(genres)
    
    for genre, play, i in zip(genres, plays, range(songNum)):
        if(not(genre in songHash)):
            songHash[genre] = []            
        songHash[genre].append({ i: play })
    """
    {'classic': [{0: 500}, {2: 150}, {3: 800}], 'pop': [{1: 600}, {4: 2500}]}
    """
    print(songHash)



testGenres = ["classic", "pop", "classic", "classic", "pop"]
testPlays = [500, 600, 150, 800, 2500]

solution(testGenres, testPlays)