def solution(dartResult):
    ss=""
    onedart=[]
    q=0
    for i in range(1,len(dartResult)):
        if dartResult[i].isdigit() and i-1!=q:
            onedart.append(dartResult[q:i])
            q=i
    onedart.append(dartResult[q:])
    
    for zzz in range(2):
        if onedart[1+zzz].count('*'):
            onedart[zzz]+='*'
    num=0
    for nnnn in range(3):
        if onedart[nnnn][1].isdigit():
            a=10
        else:
            a = int(onedart[nnnn][0])
        for zzzz in range(len(onedart[nnnn])):
            if not onedart[nnnn][zzzz].isdigit():
                if onedart[nnnn][zzzz]=="S":
                    a*=1
                elif onedart[nnnn][zzzz]=="D":
                    a = a**2
                elif onedart[nnnn][zzzz]=="T":
                    a = a**3
                elif onedart[nnnn][zzzz]=="*":
                    a *= 2
                elif onedart[nnnn][zzzz]=="#":
                    a*=-1
        num+=a
    return num
