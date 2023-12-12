from FormulasMath import sigmoid, summation

import random



class Perceptron:
    def __init__(self) -> None:
        self.score = 0
        self.threshold = None

    def output(self, wList, xList, threshould) -> int:

        if len(wList) != len(xList):
            raise ValueError("Matrix with different dimensions")

        sumWX = sum([(wList[j]*xList[j]) for j in range(0,len(wList))])

        if sumWX <= threshould:
            return 0
        else:
            return 1
        
    def training(self, num_training):
        
        for i in range(0,num_training):
            threshold = random.randint(0,10)
            score = 0

            for i in [0,1]:
                for ii in  [0,1]:
                    for iii in [0,1]:
                        output = perceptron.output(wList,[i,ii,iii], threshold)
                        score += output

            if self.score < score:
                self.score = score
                self.threshold = threshold


if __name__=="__main__":


    print(summation(lambda xw: None, [(2,2),(3,0),(1,2)]))

    """
    A: A Nara fazendo comida?
    B: A Nara no celular?
    C: A Nara safadinha?
    Output: Amo a Nara?
    """

    A = 5
    B = -2
    C = 8

    wList = [A,B,C]



