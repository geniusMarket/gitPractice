# -*- coding = utf-8 -*-
# @Time : 2021/10/30 9:32
# Author : joi
# @File : newRound.py
# @Software : PyCharm

def newRound(_float, _len):
    if isinstance(_float, float):
        if str(_float)[::-1].find('.') <= _len:
            return(_float)
        if str(_float)[-1] == '5':
            return(round(float(str(_float)[:-1]+'6'), _len))
        else:
            return(round(_float, _len))
    else:
        return(round(_float, _len))





