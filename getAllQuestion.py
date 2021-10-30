from getRandom import getRandom
def getAllQuestion(level, num):
    list = []
    for i in range(num):
        list.append(getRandom.getRandom(level))
    return list


