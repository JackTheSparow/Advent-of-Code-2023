import re

#input from file
games=open('input','r')

#12 red cubes, 13 green cubes, and 14 blue cubes
'''
#game-> true or false
#send true if possible else false
#stub
def checkCubes(game):
    #print(game)
    pattern=re.compile(r'(\d+)\s*(red|blue|green)')
    matches=pattern.findall(game)
    for match in matches:
        number,color=match
        if(color.lower()=='blue' and int(number)>14):
            return False
            break
        if(color.lower()=='red' and int(number)>12):
            return False
            break
        if(color.lower()=='green' and int(number)>13):
            return False
            break
        #print(f"Number:{number}, Color:{color}")
    return True
'''
'''
#game -> integer
#send back id of possible games in input
def returnId(game):
        gameId=re.search(r'Game (\d+):',game)
        #print(gameId.group(1))
        
        possibleCombination=checkCubes(game)
        
        if possibleCombination:
            return int(gameId.group(1))
        else:
            return 0
'''

#game -> Integer
#product of maximum cubes of each color
def getPowers(game):
    maxRed=0
    maxGreen=0
    maxBlue=0
    product=1
    pattern=re.compile(r'(\d+)\s*(red|blue|green)')
    matches=pattern.findall(game)
    #print("hello")
    matches
    for match in matches:
        number,color=match
        if(color.lower()=='blue' and int(number)>maxBlue):
            maxBlue=int(number)
            #print(int(number))
        if(color.lower()=='red' and int(number)>maxRed):
            maxRed=int(number)
            #print(int(number))
        if(color.lower()=='green' and int(number)>maxGreen):
            maxGreen=int(number)    
            #print(int(number))
    product=maxRed*maxGreen*maxBlue
    return product

#listOfGames -> Integer
#Sum of possible game ids
'''def sumOfId(games):
    totalSum=0
    for game in games:
        totalSum=totalSum+returnId(game)
    print(totalSum)'''

#listOfGames -> Integer
#Product of max cubes required for each game
def productOfMaxCubes(games):
    sumOfPowers=0
    for game in games:
        power = getPowers(game)
        sumOfPowers=sumOfPowers+power
    print(sumOfPowers)

if True:
    #sumOfId(games)
    productOfMaxCubes(games)
else:
    print("damn bruh")