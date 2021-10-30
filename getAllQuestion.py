import getRandom
def getAllQuestion(level, num):
    for i in range(num):
        list = []
        list.append(getRandom(level))
    return list


