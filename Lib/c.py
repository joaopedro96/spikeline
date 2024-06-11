#
# Name: c.py
# Function: Identifies all possible coding sequences (CDS) from an input genoma file
# Author: João Pedro da Mata Gonçalves Ribeiro
# Date: 19/05/2024
#

import sys
from Utils import FastaUtils
from Utils import LogUtils


def runModuleC(fastaData):
    LogUtils.logStatus("\nRunning SpikeLine -> c", LogUtils.PURPLE)
    cdsList = FastaUtils.getCDSList(fastaData)
    logCdsListLength(cdsList)
    FastaUtils.makeCdsFastaFiles(cdsList)
    logCdsFilesCreated()

def logCdsListLength(cdsList):
    global cdsOccurrences
    cdsOccurrences = len(cdsList)
    LogUtils.logStatus(f"{LogUtils.PINK}CDS occurrences: {LogUtils.ENDC}{cdsOccurrences}", "")


def logCdsFilesCreated():
    global cdsOccurrences
    LogUtils.logStatus(f"{LogUtils.PINK}CDS fasta files generated at: {LogUtils.ENDC}saida/cds/", "")


inputFilePath = sys.argv[1]

fastaData = FastaUtils.getFastaFileData(inputFilePath)
runModuleC(fastaData)