def chackDone(progresses):
    doneWork = 0
    while(progresses[0] >= 100):
        doneWork += 1
        progresses.pop(0)
        if(len(progresses) == 0): break

    return doneWork

def deploy(progresses,speeds):
    while(progresses[0] < 100):
        for i, task in enumerate(progresses):
            progresses[i] += speeds[i]

def solution(progresses, speeds):
    answer = []

    while(1):
        deploy(progresses, speeds)
        doneWork = chackDone(progresses)
        answer.append(doneWork)
        if(len(progresses) == 0): break
    
    return answer

testProgresses = [95, 90, 99, 99, 80, 99]
testSpeeds = [1, 1, 1, 1, 1, 1]

solution(testProgresses, testSpeeds)
