def solution(new_id):

    new_id=new_id.lower()
    zz=["-","_","."]
    ss=""
    for i in range(len(new_id)):
        if 48<=ord(new_id[i])<=57  or 97<=ord(new_id[i]) <=122 or ord(new_id[i])==45 or ord(new_id[i])== 46 or ord(new_id[i])== 95:
            ss+=new_id[i]
    new_id=ss
    
    while(new_id.count("..")):
        new_id=new_id.replace('..','.')

    new_id=new_id.rstrip('.')
    new_id=new_id.lstrip('.')

    if not len(new_id):
        new_id+="a"

    new_id=new_id[:15]
    new_id=new_id.rstrip('.')

    while len(new_id)<3:
        new_id+=new_id[len(new_id)-1]
   



    return new_id
