#
# Name: e.py
# Function: Generate the distance map from pdb file
# Author: João Pedro da Mata Gonçalves Ribeiro
# Date: 10/06/2024
#


def getFileData(filePath):
    inputFile = open(filePath)
    fileData = []
    for line in inputFile.readlines():
        formmatedLine = line.strip()
        fileData.append(formmatedLine)
        inputFile.close()
    return fileData


def getAtomsLines(fileData):
    atomLineList = []
    for line in fileData:
        if line[0:4] == "ATOM":
            atomLineList.append(line)
    return atomLineList


def getDictionary(atomData):
    atomDict = {}
    for atom in atomData:
        dictData = {}
        dictKey = atom[6:11].strip()
        dictData["nome"] = atom[12:16].strip()
        dictData['cadeia'] = atom[21].strip()
        dictData['residuo'] = atom[17:20].strip()
        dictData['numResiduo'] = atom[22:26].strip()
        dictData['x'] = float(atom[30:38].strip())
        dictData['y'] = float(atom[38:46].strip())
        dictData['z'] = float(atom[46:54].strip())
        atomDict[dictKey] = dictData    
    return atomDict


def atomDistance(atom1, atom2):
    diff_X = atom2['x'] - atom1['x']
    diff_Y = atom2['y'] - atom1['y']
    diff_Z = atom2['z'] - atom1['z']
    distance = ( (diff_X ** 2) + (diff_Y ** 2) + (diff_Z ** 2) ) ** (1/2)
    return distance


filePath = "PDB_FILE_PATH"
fileData = getFileData(filePath)
atomData = getAtomsLines(fileData)
dicionario = getDictionary(atomData)

distMatrix = []
for key_i, value_i in dicionario.items():
    distMatrix.append([])
    for key_j, value_j in dicionario.items():
        lastIndex = len(distMatrix)
        distMatrix[lastIndex - 1].append(atomDistance(value_i, value_j))

print(distMatrix)