#
# Name: FastaUtils.py
# Function: Provides general functions to aid work with fasta files
# Author: João Pedro da Mata Gonçalves Ribeiro
# Date: 18/04/2024
#

import re

def getFastaFileData(inputFilePath: str):
    fastaFile = __tryOpenFile(inputFilePath)
    if fastaFile == "FILE_NOT_FOUND_EXCEPTION": return "FILE_NOT_FOUND_EXCEPTION"

    fastaData = fastaFile.readlines()
    checkFormatExceptions = __checkIfHasFastaFormat(fastaData)
    if "EXCEPTION" in checkFormatExceptions: return checkFormatExceptions

    parsedData = { }
    dictKey = ""
    dictValue = []
    for line in fastaData:
        if line[0] == ">":
            dictKey = line.replace('>', '').strip()
            dictValue = []

        else:
            if not __sequenceHasOnlyLetters(line): return "WRONG_FASTA_FORMAT_EXCEPTION"
            dictValue.append(line.strip())
            parsedData[dictKey] = dictValue

    fastaFile.close()
    return parsedData


def makeFastaFile(fileTitle, parsedFastaData):
    fastaFile = open("./saida/" + fileTitle + ".fasta", "w")
    
    for fastaID, fastaSequences in parsedFastaData.items():
        fastaFile.write(">" + fastaID + "\n")
        for sequence in fastaSequences:
            fastaFile.write(sequence + "\n")
        
    fastaFile.close()


def makeFastaFileFromKmerList(fileTitle, kMerList):
    parsedFastaData = {}
    for index, sequence in enumerate(kMerList):
        parsedFastaData[str(index)] = [sequence]
    makeFastaFile(fileTitle, parsedFastaData)
    
    
def makeCdsFastaFiles(sequences):
    for index, sequence in enumerate(sequences):
        fastaFile = open(f"./saida/cds/coding_sequence_{index}.fasta", "w")
        fastaFile.write(f">CDS_{index}\n")
        fastaFile.write(sequence + "\n")
    fastaFile.close()


def makeCdsTempFile(sequences):
    tempFile = open(f"temp.txt", "w")
    for index, sequence in enumerate(sequences):
        tempFile.write(f">CDS_{index}\n")
        tempFile.write(sequence + "\n")
    tempFile.close()


def calcSymbolContent(symbol: str, fastaParsedData):
    fastaFullSequence = ""

    for sequence in fastaParsedData.values():
        fastaFullSequence += __joinSequenceList(sequence)
    
    symbolOccurrences = __calcOccurrences(symbol, fastaFullSequence)
    sequenceSize = len(fastaFullSequence)
    contentPercent = symbolOccurrences / sequenceSize * 100
    return contentPercent


def calcFastaSequencesLenght(fastaParsedData):
    fastaFullSequence = ""

    for sequence in fastaParsedData.values():
        fastaFullSequence += __joinSequenceList(sequence)
    
    return len(fastaFullSequence)


def getKmerList(fastaParsedData, k):
    fastaFullSequence = ""
    for sequence in fastaParsedData.values():
        fastaFullSequence += __joinSequenceList(sequence)

    step = k 
    kMerList = []
    for index in range(len(fastaFullSequence)-step+1):
        kMer = fastaFullSequence[index:index+step]
        kMerList.append(kMer)
    return kMerList



def getCDSList(fastaParsedData):
    fastaFullSequence = ""
    for sequence in fastaParsedData.values():
        fastaFullSequence += __joinSequenceList(sequence)

    transcriptSequence = __sequenceTranscription(fastaFullSequence)
    regex = "AUG.*?(?:UAG|UAA|UGA)"
    cdsList = re.findall(regex, transcriptSequence)
    return cdsList

# PRIVATE METHODS

def __checkIfHasFastaFormat(fastaData):
    if __isEmptyFile(fastaData):
        return "EMPTY_FILE_EXCEPTION"

    elif not __hasFastaFormat(fastaData):
        return "WRONG_FASTA_FORMAT_EXCEPTION"
    
    else:
        return "HAS_HEADER_AND_SEQUENCE"


def __tryOpenFile(filePath):
    try:
       inputFile = open(filePath)
       return inputFile
    except FileNotFoundError:
       return "FILE_NOT_FOUND_EXCEPTION"


def __isEmptyFile(fileData):
    hasLines = len(fileData) >= 1
    hasWords = False
    if hasLines:
        hasWords = len(fileData[0]) >= 1
    return not (hasLines and hasWords)


def __hasFastaFormat(fastaFile):
    hasSequence = len(fastaFile) >= 2
    hasHeader = fastaFile[0][0] == ">"
    return hasHeader and hasSequence


def __sequenceHasOnlyLetters(fastaSequence):
    return fastaSequence.strip().isalpha()


def __calcOccurrences(symbol: str, sequence: str):
    symbolOccurrences = 0
    for letter in symbol:
        symbolOccurrences += sequence.count(letter)
    return symbolOccurrences


def __joinSequenceList(sequence):
    joinedList = ''.join(sequence)
    return joinedList


def __sequenceTranscription(sequence):
    return sequence.replace("T", "U")