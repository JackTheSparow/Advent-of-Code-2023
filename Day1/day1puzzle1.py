#Day 1: Puzzle 1

strings=open('input','r')
sum=0

tmp="0"

for string in strings:
    no=[]
    for s in string:
        if s.isnumeric():
            no.append(s)
        if len(no)==0:
            continue
        else:
            firstNo=no[0]
            lastNo=no[-1]
            tmp=str(firstNo)+str(lastNo)
            #print(tmp)
    sum=sum+int(tmp)

print(sum)