import random


def getRandom(level):
    N = random.randint(2,10)    # 随机生成运算数个数
    res = []        # 运算数列表
    compute = ''    # 最终字符串
    option = ["+","-","*","/"]
    if level == 3:
        for i in range(N):
            num = random.uniform(1,10000)
            res.append(num)
    if level == 2:
        res = random.sample(range(1, 10000), N)
    if level == 1:
        res = random.sample(range(1, 100), N)

    for i in range(N):
        compute = compute + str(res[i]) + random.choice(option)

    return compute[:-1]
