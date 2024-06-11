#
# Name: a.py
# Function: Print GC content and sequence lenght
# Author: João Pedro da Mata Gonçalves Ribeiro
# Date: 19/05/2024
#

import sys
from Utils import FastaUtils
from Utils import LogUtils


def runModuleA(fastaData):
    LogUtils.logStatus("\nRunning SpikeLine -> a", LogUtils.PURPLE)
    logFastaSequenceLenght(fastaData)
    logFastaGCSymbolContent(fastaData)


def logFastaSequenceLenght(fastaData):
    fastaLenght = FastaUtils.calcFastaSequencesLenght(fastaData)
    LogUtils.logStatus(f"{LogUtils.PINK}Sequence lenght: {LogUtils.ENDC}{fastaLenght}", "")


def logFastaGCSymbolContent(fastaData):
    gcContent = FastaUtils.calcSymbolContent("GC", fastaData)
    formattedNumber = "{:.2f}".format(gcContent)
    LogUtils.logStatus(f"{LogUtils.PINK}GC content: {LogUtils.ENDC}{formattedNumber}%", "")


inputFilePath = sys.argv[1]

fastaData = FastaUtils.getFastaFileData(inputFilePath)
runModuleA(fastaData)