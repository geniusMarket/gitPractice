# // 获取年级，返回等级
# getGrade(string grade) {
#     return level(int)
# }
def getGrade(grade):
    if grade == '一年级' or grade == '二年级':
        return 1
    if grade == '三年级' or grade == '四年级':
        return 2
    if grade == '五年级' or grade == '六年级':
        return 3
