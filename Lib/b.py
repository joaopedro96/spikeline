#
# Name: b.py
# Function: Get the fasta data and divides the sequence in k-Mer with size 31
# Author: João Pedro da Mata Gonçalves Ribeiro
# Date: 19/05/2024
#

import sys
from Utils import FastaUtils
from Utils import LogUtils


def runModuleB(fastaData):
    LogUtils.logStatus("\nRunning SpikeLine -> b", LogUtils.PURPLE)
    kMerSequenceList = getKmerSequences(fastaData, 31)
    logKMerListSequenceLength(kMerSequenceList)
    makeKmerFastaFile("reads", kMerSequenceList)
    logFastaFileCreated("reads.fasta")


def getKmerSequences(fastaData, k):
    kMerSequences = FastaUtils.getKmerList(fastaData, k)
    return kMerSequences


def makeKmerFastaFile(fileName, kMerSequenceList):
    FastaUtils.makeFastaFileFromKmerList(fileName, kMerSequenceList)


def logKMerListSequenceLength(kMerList):
    kMerListLenght = len(kMerList)
    LogUtils.logStatus(f"{LogUtils.PINK}kMer list sequence lenght: {LogUtils.ENDC}{kMerListLenght}", "")


def logFastaFileCreated(outpuFiletPath):
    LogUtils.logStatus(f"{LogUtils.PINK}kMer fasta file generated at: {LogUtils.ENDC}saida/{outpuFiletPath}", "")


inputFilePath = sys.argv[1]

fastaData = FastaUtils.getFastaFileData(inputFilePath)
runModuleB(fastaData)