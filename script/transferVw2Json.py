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
    #data = []
    out_f = open(output_file, "w")
    out_f.write('[')
    cnt = 0
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
            if cnt > 0:
                out_f.write(',')
            out_f.write(json.dumps(dic))
            cnt += 1
            if cnt % 10000 == 0:
                print("finished " + str(cnt))
            #data.append(dic)
    #with open(output_file, "w") as f:
    #    f.write(json.dumps(data))
    out_f.write("]")
    out_f.close()
if __name__ == "__main__":
    main()
