from arrayPopulation import arrayPopulation 

class populateArray:

    def printResult(self,resultArr):
        for i in resultArr:
            print(i)

    def main(self):
        self.resultArr = arrayPopulation.arrayPopulate()
        self.printResult(self.resultArr)

if __name__=='__main__':
    obj = populateArray()
    obj.main()