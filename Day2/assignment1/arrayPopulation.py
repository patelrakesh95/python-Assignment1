import sys

class arrayPopulation:

    def arrayPopulate():
        resultArr = []
        try:
            print("Please enter the array 1 size : ")
            arrSize1 = int(input())
            print("Please enter the array 1 size : ")
            arrSize2 = int(input())
            if arrSize1 != arrSize2:
                print("Please enter same array size.")
            else:
                try:
                    arr1 = []
                    arr2 = []
                    for i in range(arrSize1):
                        print(f"Enter first array value of {i+1} :")
                        arr1.append(int(input()))
                    for i in range(arrSize2):
                        print(f"Enter second array value of {i+1} :")
                        arr2.append(int(input()))
                    for i in range(arrSize1):
                            resultArr.append(arr1[i])
                            resultArr.append(arr2[i])
                except expression as identifier:
                    print("Please enter valid data.")
        except:
            print("Please enter valid array size.")
            sys.exit(1)
        return resultArr 
