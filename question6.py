import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None
import random

class question6:
    def __init__(self, path_count, generatedInput, targetRange):
        self.path_count = path_count
        self.generatedInput = generatedInput
        self.targetRange = targetRange

    def createPaths(self):
        array = np.zeros((self.path_count, self.path_count - 1))
        array = [['' for n in row] for row in array]
        for i in range(self.path_count):
            for j in range(self.path_count - 1):
                if i < j:
                    array[i][j] = ' '
                if i == j-1:
                    array[i][j] = 'x'
        self.paths = pd.DataFrame(columns=np.arange(0, self.path_count - 1), data=array)
        return self.paths

    def generateMulticastInputs(self):
        randomInputs = []
        randomOutputs = []
        for i in range(self.generatedInput):
            randomInput = random.randint(0, self.path_count-1)
            while randomInput in randomInputs:
                randomInput = random.randint(0, self.path_count - 1)
            randomInputs.append(randomInput)
            randomOutputSize = random.randint(1, self.targetRange)
            currentRandomOutputs = []
            for j in range(randomOutputSize):
                randomOutput = random.randint(0, self.path_count-1)
                while randomOutput == randomInput or randomOutput in currentRandomOutputs:
                    randomOutput = random.randint(0, self.path_count-1)
                currentRandomOutputs.append(randomOutput)
            print('Generated Input: ', randomInput, '\tGenerated Outputs: ', currentRandomOutputs)

            randomOutputs.append(currentRandomOutputs)
        return randomInputs, randomOutputs

    def extendedOneSidedMeshAlgorithm(self, randomInputs, randomOutputs):
        for i in range(len(randomInputs)):
            for j in range(len(randomOutputs[i])):
                encounterPoint = min(randomInputs[i], randomOutputs[i][j])
                endPoint = max(randomInputs[i], randomOutputs[i][j])
                if not '<' in self.paths[0][endPoint]:
                    if randomInputs[i] < randomOutputs[i][j]:
                        for k in range(0, encounterPoint):
                            self.paths[k][encounterPoint] += '>'
                        for k in range(encounterPoint, endPoint+1):
                            self.paths[encounterPoint][k] += 'v'
                        for k in range(0, encounterPoint):
                            self.paths[k][endPoint] += '<'
                    if randomInputs[i] > randomOutputs[i][j]:
                        for k in range(0, encounterPoint):
                            self.paths[k][encounterPoint] += '<'
                        for k in range(encounterPoint, endPoint+1):
                            self.paths[encounterPoint][k] += '^'
                        for k in range(0, encounterPoint):
                            self.paths[k][endPoint] += '>'
                else:
                    for k in range(0, encounterPoint):
                        self.paths[k][encounterPoint] += '#'
                    for k in range(encounterPoint, endPoint + 1):
                        self.paths[encounterPoint][k] += '#'
                    for k in range(0, encounterPoint):
                        self.paths[k][endPoint] += '#'
        return self.paths


if __name__ == "__main__":
    q = question6(path_count=16, generatedInput=3, targetRange=4)
    path = q.createPaths()
    randomInputs, randomOutputs = q.generateMulticastInputs()
    generatedPath = q.extendedOneSidedMeshAlgorithm(randomInputs=randomInputs, randomOutputs=randomOutputs)
    print(generatedPath)




