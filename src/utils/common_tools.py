import os
import sys
import networkx as nx
import re
import json
import numpy as np
import math
from datetime import datetime
from Queue import Queue
from sklearn.preprocessing import MultiLabelBinarizer

class CommonTools(object):
    @staticmethod
    def dict_add(d, key, add):
        if key in d:
            d[key] += add
        else:
            d[key] = add

    @staticmethod
    def load_fea(file_path):
        X = []
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                items = line.split()
                if len(items) < 1:
                    continue
                X.append([float(item) for item in items])
        return np.array(X)


    @staticmethod
    def symlink(src, dst):
        try:
            os.symlink(src, dst)
        except OSError:
            os.remove(dst)
            os.symlink(src, dst)


    @staticmethod
    def load_json_file(file_path):
        with open(file_path, "r") as f:
            s = f.read()
            s = re.sub('\s',"", s)
        return json.loads(s)

    @staticmethod
    def get_time_str():
        return datetime.now().strftime("%Y-%m-%d-%H:%M:%S.%f")

    @staticmethod
    def append_to_file(file_path, s):
        with open(file_path, "a") as f:
            f.write(s)

    @staticmethod
    def load_ground_truth(file_path):
        lst = []
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if len(line) == 0:
                    continue
                items = line.split()
                lst.append([int(i) for i in items])
        lst.sort()
        return [i[1] for i in lst]
    
    @staticmethod
    def load_multilabel_ground_truth(file_path):
        lst = []
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if len(line) == 0:
                    continue
                items = line.split()
                lst.append([int(i) for i in items])
        lst.sort()
        lst = [i[1:] for i in lst]
        mlb = MultiLabelBinarizer()
        return mlb.fit_transform(lst)

    @staticmethod
    def load_onehot_ground_truth(file_path):
        lst = []
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if len(line) == 0:
                    continue
                items = line.split()
                lst.append([int(i) for i in items])
        lst.sort()
        return np.array([i[1:] for i in lst], dtype=int)

