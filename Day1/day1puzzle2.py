#Day 1: Puzzle 2
strings=open('input2','r')
sum=0

tmp="0"

def convertWordToNumber(word):
    switch_dict={
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9
    }
    return switch_dict.get(word,'default case')

def filterValues(string):
    keywords=["one", "two", "three", "four","five","six","seven","eight","nine"]
    found_words=[]

    #create substrings with brute force to check with keywords
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            substring=string[i:j]
            if substring in keywords:
                no=convertWordToNumber(substring)
                found_words.append(no)
            if substring.isnumeric():
                found_words.append(substring)
    return found_words    



no=[]
for string in strings:
    no.clear()
    no.extend(filterValues(string))
    if len(no)==0:
        continue
    else:
        firstNo=no[0]
        lastNo=no[-1]
        tmp=str(firstNo)+str(lastNo)
        #print(tmp)
    sum=sum+int(tmp)

print(sum)