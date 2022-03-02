def solution(N, stages):
    answer = []
    xxx=[]
    stages.sort()
    z=len(stages)
    for i in range(N+1):
        if z!=0:
            answer.append(stages.count(i)/z)
        else:
            answer.append(0)
        z-=stages.count(i)
    answer=answer[1:]
    
    for i in range(len(answer)):
        xxx.append(answer.index(max(answer))+1)
        answer[answer.index(max(answer))]=-1

    return xxx
