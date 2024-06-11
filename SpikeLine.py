#
# Name: SpikeLine.py
# Function: Runs pipeline
# Author: João Pedro da Mata Gonçalves Ribeiro
# Date: 18/05/2024
#

import os
import sys
from Lib.Utils import LogUtils
from Lib.Utils import FastaUtils


def readInputArgs():
   for index, arg in enumerate(sys.argv):
      if index % 2 == 1:

         if arg == "-h" or arg == "--help":
            LogUtils.logHelpInstructions()
            exit()

         elif arg == "-i" or arg == "--input":
            global inputFilePath
            inputFilePath = getArgumentValue(sys.argv, index + 1)
            break

         else:
            global unknownArg
            unknownArg = arg
            handleInputException(f"INPUT_UNKNOWN_COMMAND")


def getArgumentValue(argumentList, index):
  try:
     return argumentList[index]
  except IndexError:
    handleInputException("INPUT_PATH_NOT_FOUND_IN_COMMAND")


def handleInputException(inputExceptionType):
    errorText = ""

    if inputExceptionType == "INPUT_PATH_NOT_FOUND_IN_COMMAND":
       errorText = "[!] Input file path not found in command line."
    
    elif inputExceptionType == "INPUT_UNKNOWN_COMMAND":
       global unknownArg
       errorText = f"[!] Unknown command: `{unknownArg}`"

    LogUtils.logStatus(errorText, LogUtils.RED)
    LogUtils.logHelpInstructions()
    exit()


def handleExceptionError(exceptionType):
    errorText = ""
    if exceptionType == "FILE_NOT_FOUND_EXCEPTION":
       global inputFilePath
       errorText = f"[!] File not found: `{inputFilePath}`"
       
    elif exceptionType == "EMPTY_FILE_EXCEPTION":
       errorText = "[!] Empty File: Input file has no data"

    elif exceptionType == "WRONG_FASTA_FORMAT_EXCEPTION":
       errorText ="[!] Format error: input file it is not in fasta format"

    LogUtils.logStatus(errorText, LogUtils.RED)
    LogUtils.logStatus("\nSpikeLine finished with errors", LogUtils.BOLD)
    exit()
   

def logLoadFastaFileStatus():
    global inputFilePath
    LogUtils.logStatus(f"Input file path defined as `{inputFilePath}`", "")
    LogUtils.logStatus(f"Trying to load fasta file `{inputFilePath}`", "")
    fastaData = FastaUtils.getFastaFileData(inputFilePath)
    if (type(fastaData) == str) and ("EXCEPTION" in fastaData): handleExceptionError(fastaData)
    LogUtils.logStatus(f"Fasta file loaded with success", "")

   
def runSpikeLine():
   LogUtils.logStatus("Running SpikeLine", LogUtils.GREEN)
   logLoadFastaFileStatus()
   os.system("python3 Lib/a.py " + inputFilePath)
   os.system("python3 Lib/b.py " + inputFilePath)
   os.system("python3 Lib/c.py " + inputFilePath)
   os.system("python3 Lib/d.py " + inputFilePath)
   LogUtils.logStatus("\nSpikeLine finished with success", LogUtils.BOLD)


readInputArgs()
runSpikeLine()