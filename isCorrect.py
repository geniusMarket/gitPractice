from newRound import newRound
def isCorrect(question, answer):
    correctAnswer = eval(question)
    if newRound(correctAnswer, 2) == newRound(answer, 2):
        return True
    else:
        return False