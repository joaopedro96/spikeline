#
# Name: d.py
# Function: Get the spike gene code
# Author: João Pedro da Mata Gonçalves Ribeiro
# Date: 10/06/2024
#

import sys
from Utils import FastaUtils
from Utils import LogUtils
from Utils import AminoAcidUtils


def runModuleD(fastaData):
    LogUtils.logStatus("\nRunning SpikeLine -> d", LogUtils.PURPLE)
    proteicChainCode = AminoAcidUtils.getProteicChainCode(fastaData)
    spikeGeneCode = AminoAcidUtils.getSpikeGeneCode(proteicChainCode)
    logSpikeGeneCode(spikeGeneCode)
    makeSpikeGeneFastaFile(spikeGeneCode)
    logSpikeGeneFastaFile()


def makeSpikeGeneFastaFile(spikeGeneCode):
    parsedFastaData = {"spike_gene": [spikeGeneCode]}
    FastaUtils.makeFastaFile("spike", parsedFastaData)


def logSpikeGeneCode(spikeGeneCode):
    LogUtils.logStatus(f"{LogUtils.PINK}Spike gene code: {LogUtils.ENDC}{spikeGeneCode}", "")


def logSpikeGeneFastaFile():
    LogUtils.logStatus(f"{LogUtils.PINK}Spike gene fasta file generated at: {LogUtils.ENDC}saida/spike.fasta", "")


inputFilePath = sys.argv[1]

fastaData = FastaUtils.getFastaFileData(inputFilePath)
runModuleD(fastaData)