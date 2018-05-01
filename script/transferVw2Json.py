import sys
import os
import json
import argparse
from env import *

def main():
    parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)
    parser.add_argument('--input_file', type = str, required = True)
    args = parser.parse_args()
    input_file = os.path.join(ORIGIN_DATA_PATH, args.input_file)
    output_file = input_file + ".json"
    with open(input_file, "r") as f:
        for line in f:
            line = line.strip()
            if len(line) == 0:
                continue
            items = line.split('|')
            print items

if __name__ == "__main__":
    main()
