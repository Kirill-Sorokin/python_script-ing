import os, json, shutil, sys
from subprocess import PIPE, run

def main(source, target):
    pass

if __name__ == "__main__":
    args = sys.argv
    # print(args)
    if len(args) != 3:
        raise Exception("You must pass a source & target directory - only.")
    
    source, target = args[1:]
    main(source, target)