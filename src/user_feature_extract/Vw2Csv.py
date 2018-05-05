import os
import sys
import numpy as np

from utils.common_tools import CommonTools as ct

def user_feature_extract(params, static_info):
    if "start_line" in params:
        st = params["start_line"]
    else:
        st = 1
    if "end_line" in params:
        ed = params["end_line"]
    else:
        ed = sys.maxint
    default = float(params["default"])

    feas_merge = params["feature_merge"]
    feas_rsv = params["feature_reservation"]
    feas_info = static_info["user_feature_info"]["feature_info"]

    order_list = [None] * len(feas_rsv)
    for key, value in feas_rsv.items():
        order_list[value["order"]] = key
        value["dim"] = 1
        if key in feas_info and feas_info[key]["categorical"] and feas_info[key]["dim"] > 2:
            value["dim"] = feas_info[key]["dim"]

    for key, value in feas_merge.items():
        if feas_info[key]["dim"] > 2:
            feas_rsv[value]["dim"] = feas_info[key]["dim"]
    #print order_list
    #print feas_rsv

    pre_dim = 0
    for key in order_list:
        feas_rsv[key]["st"] = pre_dim
        pre_dim += feas_rsv[key]["dim"]

    res = np.ones((ed - st + 1, pre_dim), dtype = np.float32) * default
    with open(os.path.join(static_info["data_path"],
        params["input_file"]), "r") as f:
        cnt = 0
        for line in f:
            if (cnt < st - 1):
                cnt += 1
                continue
            if (cnt >= ed):
                break
            line = line.strip()
            if len(line) == 0:
                continue
            items = line.split('|')
            vis = set()
            for item in items:
                item = item.strip()
                if len(item) == 0:
                    continue
                its = item.split()
                if len(its) <= 1:
                    continue
                key = its[0]
                flag = True
                if key in feas_merge:
                    if feas_merge[key] in vis:
                        flag = False
                    else:
                        vis.add(feas_merge[key])
                    key = feas_merge[key]
                elif key not in feas_rsv:
                    continue
                if feas_rsv[key]["is_one_hot"]:
                    if flag:
                        for i in xrange(feas_rsv[key]["st"], feas_rsv[key]["st"] + feas_rsv[key]["dim"]):
                            res[cnt - st + 1][i] = 0
                    for it in its[1:]:
                        res[cnt - st + 1][feas_rsv[key]["st"] + int(it) - 1] = 1
                else:
                    res[cnt - st + 1][feas_rsv[key]["st"]] = float(its[1])
            cnt += 1
    file_path = os.path.join(static_info['res_path'], 'user_features_' + static_info["time_str"] + ".csv")
    np.savetxt(
            fname = file_path,
            X = res,
            fmt = '%.2f',
            delimiter = ',')
    ct.symlink(file_path, os.path.join(static_info['res_path'], 'new_user_features'))
