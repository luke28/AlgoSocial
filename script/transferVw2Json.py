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
    data = []
    with open(input_file, "r") as f:
        for line in f:
            line = line.strip()
            if len(line) == 0:
                continue
            items = line.split('|')
            dic = {}
            for item in items:
                item = item.strip()
                if len(item) == 0:
                    continue
                its = item.split()
                if len(its) <= 1:
                    continue
                if len(its) == 2:
                    dic[its[0]] = int(its[1])
                else:
                    dic[its[0]] = []
                    for it in its[1:]:
                        dic[its[0]].append(int(it))
            data.append(dic)
    with open(output_file, "w") as f:
        f.write(json.dumps(data))
if __name__ == "__main__":
    main()
