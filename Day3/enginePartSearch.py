#any number adjacent to a symbol, even diagonally
#sum of all of the part numbers in the engine schematic
'''
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''

#char positionPerLine=141

import re 

engines=open('testinput','r')
specialPosition=[]
totalSum=0

#string-> ListOfNumber
#create list of positions with special symbols
def mapOfSymbols(string,index):
    while len(specialPosition) <= index:
        specialPosition.append([])

    for position in range(len(string)):
        specialRow=[]
        char=string[position]
        #check if char is special
        if char.isascii() and not char.isalnum() and char !='.' and not char.isspace():
            #add special symbol position in array
            #if not(position in specialRow):
            #specialRow.append(position)
            #print(position)
            #print("position:",position," char:",char)
            specialPosition[index].extend([position])
    #create position list of special symbols

index=0 #line number
for string in engines:
    mapOfSymbols(string,index)
    index+=1

engines2=open('testinput','r')

#string-> ListOfNumber
#find list of number in string
def findNumbers(string):
    numbers_with_indices=[]
    for match in re.finditer(r'\d+', string):
        number = match.group()
        start_index = match.start()
        end_index = match.end() - 1

        #Calculate 2D array indices
        row=start_index // len(string.splitlines())
        col=start_index % len(string.splitlines())
        
        numbers_with_indices.append((number, start_index, end_index, row, col))
    return numbers_with_indices



for string in engines2:
    #find number in string
    numbersAndPosition=(findNumbers(string))
    #print(numbers)
    for number,start,end,row,col in numbersAndPosition:
        #check 1st digit
        #print("no:",number," start:",start," end:",end)
        
        print(f"Position of {number}:[{row}][{col}]")
                

print(totalSum)