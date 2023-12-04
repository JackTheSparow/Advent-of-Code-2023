import re

games=open('input','r')
totalPoints=0

#card->Integer
#calculate point for each card
def calculateCardPoint(card):
    finalPoints=0
    multiplier=1
    winNoStr=""
    ourNoStr=""
    match = re.match(r'.*?(\d+(?:\s+\d+)*) \|\s+(\d+(?:\s+\d+)*)', card)
    if match:
        winNoStr=match.group(1)
        ourNoStr=match.group(2)
        
    winNo = list(map(int, winNoStr.split()))
    ourNo = list(map(int, ourNoStr.split()))

    for our in ourNo:
        for win in winNo:
            if our==win:
                finalPoints=multiplier
                multiplier=2*multiplier 
    return finalPoints


#games->Integer
#calculate sum of points
def sumOfPoints(games):
    global totalPoints
    for card in games:
        point=0
        point=calculateCardPoint(card)
        totalPoints=totalPoints+point
        #print(totalPoints)
    print(totalPoints)    
    
sumOfPoints(games)