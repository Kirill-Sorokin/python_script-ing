import os, json, shutil, sys
from subprocess import PIPE, run


GAME_DIR_PATTERN = "game"

def find_all_game_paths(source):
    game_paths = []
    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                game_paths.append(path)
        break
    return game_paths

def main(source, target):
    cwd = os.getcwd()
    # "C://..." + .... <- 'String concatenation': different OS have different path dividers, therefore don't do this.
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)
    game_paths = find_all_game_paths(source_path)
    # print(game_paths)

if __name__ == "__main__":
    args = sys.argv
    # print(args)
    if len(args) != 3:
        raise Exception("You must pass a source & target directory - only.")
    
    source, target = args[1:]
    main(source, target)