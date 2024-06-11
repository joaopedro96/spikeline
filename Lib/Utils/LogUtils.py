#
# Name: LogUtils.py
# Function: Set custom prints on terminal
# Author: João Pedro da Mata Gonçalves Ribeiro
# Date: 18/05/2024
#

PURPLE = '\033[95m'
PINK = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def logStatus(msgText, msgColor):
    print(f"{msgColor}{msgText}{ENDC}")


def logHelpInstructions():
   print(f"""
    {UNDERLINE}Usage:{ENDC}

        {GREEN}python3 SpikeLine.py -i "file_path"{ENDC}

    {UNDERLINE}Commands:{ENDC}

        {PINK}-i --input{ENDC}      File path that contains the genome in fasta format 
        {PINK}-h --help{ENDC}       List of instructions to provide informations about this pipeline
    """
)