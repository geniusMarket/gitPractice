from getRandom import getRandom
def getAllQuestion(level, num):
    list = []
    for i in range(num):
        list.append(getRandom(level))
    return list


