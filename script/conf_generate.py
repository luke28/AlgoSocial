#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-02 20:37:57
# @Author  : Jipeng Huang (jphuang94@pku.edu.cn)
# @Link    : http://blog.csdn.net/wr339988/
# @Version : $Id$

import json

fulldata = {}
fulldata['columns'] = ['uid', 'age', 'gender', 'marriageStatus', 'education', 'consumptionAbility',
                       'LBS', 'interest1', 'interest2', 'interest3', 'interest4', 'interest5',
                       'kw1', 'kw2', 'kw3', 'topic1', 'topic2', 'topic3', 'appIdInstall',
                       'appIdAction', 'ct', 'os', 'carrier', 'house']

categorical = ['gender', 'marriageStatus', 'education', 'consumptionAbility',
               'LBS', 'interest1', 'interest2', 'interest3', 'interest4', 'interest5',
               'kw1', 'kw2', 'kw3', 'topic1', 'topic2', 'topic3', 'appIdInstall',
               'appIdAction', 'ct', 'os', 'carrier', 'house']
islist = ['interest1', 'interest2', 'interest3', 'interest4', 'interest5',
          'kw1', 'kw2', 'kw3', 'topic1', 'topic2', 'topic3', 'ct']
numerical = ['age']

data = {}
for fea in fulldata['columns']:
    if fea not in data:
        data[fea] = {}
        if fea in categorical:
            data[fea]['categorical'] = True
        else:
            data[fea]['categorical'] = False
        if fea in islist:
            data[fea]['islist'] = True
        else:
            data[fea]['islist'] = False
        if fea in numerical:
            data[fea]['numerical'] = True
        else:
            data[fea]['numerical'] = False

# features = sort_by_value(data)
fulldata['features'] = data

path = "/home/foresee/Documents/TencentAlgo/AlgoSocial/origin_data/features.conf"
jsonfile = open(path, 'w')
jsonfile.write(json.dumps(fulldata, ensure_ascii=False, indent=2))
