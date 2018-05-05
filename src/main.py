import os
import sys
import re
import json
import math
import argparse
import time
import subprocess
import numpy as np
import networkx as nx
import tensorflow as tf
import datetime
from operator import itemgetter
import random

from utils.env import *
#from utils.metric import Metric
from utils.data_handler import DataHandler as dh
from utils.common_tools import CommonTools as ct

FILE_PATH = os.path.dirname(os.path.abspath(__file__))


def init(params):
    static_info = {}
    random.seed(params["random_seed"])
    np.random.seed(params["np_seed"])
    user_feature_conf = ct.load_json_file(os.path.join(CONF_PATH, params["user_feature_conf"]))
    static_info["user_feature_info"] = dh.user_feature_info_extract(user_feature_conf)
    del user_feature_conf
    static_info["time_str"] = ct.get_time_str()
    static_info["data_path"] = DATA_PATH
    static_info["res_path"] = RES_PATH
    return static_info


def main():
    parser = argparse.ArgumentParser(
                formatter_class = argparse.RawTextHelpFormatter)
    #parser.add_argument('--operation', type = str, default = "all", help = "[all | init | train | metric | draw]")
    parser.add_argument('--conf', type = str, default = "test")
    args = parser.parse_args()
    params = ct.load_json_file(os.path.join(CONF_PATH, args.conf + ".json"))
    static_info = init(params["static_info"])

    for module in params["run_modules"]:
        mdl_name = module["func"]
        mdl_params = module["params"]
        mdl = __import__(mdl_name + '.' + mdl_params["func"], fromlist = [mdl_name])
        getattr(mdl, mdl_name)(mdl_params, static_info)


def main_old():

    parser = argparse.ArgumentParser(
                formatter_class = argparse.RawTextHelpFormatter)
    parser.add_argument('--operation', type = str, default = "all", help = "[all | init | train | metric | draw]")
    parser.add_argument('--conf', type = str, default = "default")
    args = parser.parse_args()
    params = dh.load_json_file(os.path.join(CONF_PATH, args.conf + ".json"))

    metric_path_pre = os.path.join(RES_PATH, args.conf)
    if os.path.exists(metric_path_pre) == False:
        os.mkdir(metric_path_pre)
    output_path = os.path.join(metric_path_pre, dh.get_time_str())
    metric_path = output_path + "_metric"

    def metric(embeddings):
        if "metrics" not in params:
            return
        for metric in params["metrics"]:
            res = getattr(Metric, metric["func"])(embeddings, metric)
            dh.append_to_file(metric_path, str(res) + "\n")
            print res
    dh.symlink(metric_path, os.path.join(metric_path_pre, "new_metric"))

    if "drawers" in params:
        draw_path = output_path + "_draw"
        if os.path.exists(draw_path) == False:
            os.mkdir(draw_path)
    draw_cnt = [0]
    def draw(embeddings):
        if "drawers" not in params:
            return
        for drawer in params['drawers']:
            getattr(Metric, drawer["func"])(embeddings, drawer, draw_path, draw_cnt[0])
        draw_cnt[0] += 1

    if args.operation == "all":
        G, embeddings, weights = __import__(
                "init." + params["init"]["func"],
                fromlist = ["init"]
                ).init(params["init"], metric, output_path, draw)
        __import__(
                "dynamic_loop." + params["main_loop"]["func"],
                fromlist = ["dynamic_loop"]
                ).loop(params["main_loop"], G, embeddings, weights, metric, output_path, draw)
    elif args.operation == "init":
        G, embeddings, weights = __import__("init." + params["init"]["func"], fromlist = ["init"]).init(params["init"], metric, output_path, draw)
    elif args.operation == "draw":
        pass
    else:
        print "Not Support!"

if __name__ == "__main__":
    main()
