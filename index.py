import sys
import getopt
from os import listdir, system
from os.path import isfile, join


def main():
    argv = sys.argv[1:]
    try:
        directory = None
        excluded = None
        opts, _ = getopt.getopt(argv, "p:e:", ["path=", "exclude="])
        for opt, arg in opts:
            if opt in ["-p", "--path"]:
                directory = arg
            elif opt in ["-e", "--exclude"]:
                excluded = arg

        run_files(directory, excluded)
    except:
        print("error")


def run_files(directory, excluded):
    try:
        all_scripts = [join(directory, f) for f in listdir(
            directory) if isfile(join(directory, f)) and f != excluded]

        for script in all_scripts:
            system('python "' + script + '"')
    except:
        pass


if __name__ == "__main__":
    main()
