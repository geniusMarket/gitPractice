from getGrade import getGrade
from getAllQuestion import getAllQuestion
from outResult import outResult
from isCorrect import isCorrect

if __name__ == '__main__':
    print('请输入你的年级：')
    Grade = input() # 输入str 年级
    level = getGrade(Grade)

    print('请输入题目数：')
    num = int(input())
    allQuestion = getAllQuestion(level,num)

    WrongNum = 0
    for question in allQuestion:
        outResult() # 打印题目
        answer = eval(input())
        if  isCorrect(question,answer) == False:
            WrongNum += 1

    print('结束！错了{}题哦'.format(WrongNum))
