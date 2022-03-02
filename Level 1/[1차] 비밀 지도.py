def solution(n, arr1, arr2):       
    def intwo(n,a):
        zz=""

        for qqq in range(a):
            if n>=2**(a-1-qqq):
                n-=2**(a-1-qqq)
                zz+="#"
            else:
                zz+=" "
        return zz
    answer=[]
    for i in range(n):
        q=""
        for xx in range(n):
            if intwo(arr1[i],n)[xx] =="#" or intwo(arr2[i],n)[xx]== "#":
                q+="#"
            else:
                q+=" "
        answer.append(q)

    
    return answer
