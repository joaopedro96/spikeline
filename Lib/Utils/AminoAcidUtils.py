#
# Name: AminoAcidUtils.py
# Function: ???
# Author: João Pedro da Mata Gonçalves Ribeiro
# Date: 19/05/2024
#

import re

rnaDictionary = {
    "UUU": "F",
    "UUC": "F",
    "UUA": "L",
    "UUG": "L",
    "UCU": "S",
    "UCC": "S",
    "UCA": "S",
    "UCG": "S",
    "UAU": "Y",
    "UAC": "Y",
    "UAA": "",
    "UAG": "",
    "UGU": "C",
    "UGC": "C",
    "UGA": "",
    "UGG": "W",
    "UGW": "W",
    "CUU": "L",
    "CUC": "L",
    "CUA": "L",
    "CUG": "L",
    "CCU": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "CAU": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "CGU": "R",
    "CGC": "R",
    "CGA": "R",
    "CGR": "R",
    "CGG": "R",
    "AUU": "I",
    "AUC": "I",
    "AUA": "I",
    "AUG": "M",
    "ACU": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "AAU": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "AGU": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GUU": "V",
    "GUC": "V",
    "GUA": "V",
    "GUG": "V",
    "GCU": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "GAU": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "GGU": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G"
}


def getProteicChainCode(fastaParsedData):
    step = 3
    codedRna = ""
    fastaFullSequence = ""
    for sequence in fastaParsedData.values():
            fastaFullSequence += __joinSequenceList(sequence)

    transcriptSequence = __sequenceTranscription(fastaFullSequence)

    for index in range(0, len(transcriptSequence), step):
        aa = transcriptSequence[index:index + step]
        if len(aa) == 3:
             codedRna += rnaDictionary[aa]
    return codedRna


def getSpikeGeneCode(proteicChainCode):
     regex = "G(?:R|K|H){2}(?:D|E){1}G"
     spikeGeneCode = re.findall(regex, proteicChainCode)
     if len(spikeGeneCode) > 0:
          return spikeGeneCode[0]
     else:
          return "Gene not found"


def __joinSequenceList(sequence):
    joinedList = ''.join(sequence)
    return joinedList


def __sequenceTranscription(sequence):
    return sequence.replace("T", "U")