def solution(numbers, hand):
    presentrg=10
    presentle=12
    answer=''
            
    for i in range(len(numbers)):
        if numbers[i]==0:
            numbers[i]=11
        if numbers[i]%3==1 :
            presentle=numbers[i]
            answer+="L"
        elif numbers[i]%3==0:
            presentrg=numbers[i]
            answer+="R"

        else :
            a=max(presentrg,numbers[i])-min(presentrg,numbers[i])
            b=max(presentle,numbers[i])-min(presentle,numbers[i])

            a=a//3 + a%3
            b=b//3 + b%3

            if a==b and hand == "right":
                presentrg=numbers[i]
                answer+="R"
            elif a>b:
                presentle=numbers[i]
                answer+="L"
            elif a<b:
                presentrg=numbers[i]
                answer+="R"
            else:
                presentle=numbers[i]
                answer+="L"



    return answer
