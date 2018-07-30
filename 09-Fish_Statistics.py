import re

fish_str = input()

fish_pattern = r"(?P<tail>>*)<(?P<body>\(+)(?P<status>['\-x])>"
fish_list = []

matches = re.finditer(fish_pattern, fish_str)
for match in matches:
    fish_list.append(match)


def findTailType(tailStr):
    tail_len = len(tailStr)
    if tail_len > 5:
        return 'Long'
    elif tail_len > 1:
        return 'Medium'
    elif tail_len == 1:
        return 'Short'
    else:
        return 'None'

def findBodyType(bodyStr):
    body_len = len(bodyStr)
    if body_len > 10:
        return 'Long'
    elif body_len > 5:
        return 'Medium'
    else:
        return 'Short'

def calcTailLen(tailStr):
    tail_len = 2 * len(tailStr)
    tail_len_str = ''
    if tail_len != 0:
        tail_len_str = "(" + str(tail_len) + " cm)"
    return tail_len_str

def calcBodyLen(bodyStr):
    body_len = 2 * len(bodyStr)
    body_len_str = ''
    if body_len != 0:
        body_len_str = "(" + str(body_len) + " cm)"
    return body_len_str

def findFishStatus(statusStr):
    if statusStr == '\'':
        return 'Awake'
    elif statusStr == '-':
        return 'Asleep'
    else:
        return 'Dead'

if fish_list == []:
    print('No fish found.')
else:
    for i in range(0, len(fish_list)):
        print(f'Fish {i+1}: {fish_list[i].group()}')
        print(f'  Tail type: {findTailType(fish_list[i].group("tail"))} {calcTailLen(fish_list[i].group("tail"))}')
        print(f'  Body type: {findBodyType(fish_list[i].group("body"))} {calcBodyLen(fish_list[i].group("body"))}')
        print(f'  Status: {findFishStatus(fish_list[i].group("status"))}')