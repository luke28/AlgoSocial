import pandas as pd
import numpy as np
import json

base_path = "/home/foresee/Documents/TencentAlgo/AlgoSocial/"
df = pd.read_json(base_path + 'origin_data/userFeature_sample.data.json')
df = df.reindex(columns=['uid', 'age', 'gender', 'marriageStatus', 'education', 'consumptionAbility',
                         'LBS', 'interest1', 'interest2', 'interest3', 'interest4', 'interest5',
                         'kw1', 'kw2', 'kw3', 'topic1', 'topic2', 'topic3', 'appIdInstall',
                         'appIdAction', 'ct', 'os', 'carrier', 'house'])
df.head().to_csv(base_path + 'origin_data/userFeature_sample.csv', index=False)
exit()
# print(df.head())
# interest = df[['interest1', 'interest2',
#                'interest3', 'interest4', 'interest5']]
it_set = set()


def cnt_interest(x):
    if isinstance(x['interest1'], list):
        for num in x['interest1']:
            it_set.add(num)
    else:
        it_set.add(x['interest1'])
    if isinstance(x['interest2'], list):
        for num in x['interest2']:
            it_set.add(num)
    else:
        it_set.add(x['interest2'])
    if isinstance(x['interest3'], list):
        for num in x['interest3']:
            it_set.add(num)
    else:
        it_set.add(x['interest3'])
    if isinstance(x['interest4'], list):
        for num in x['interest4']:
            it_set.add(num)
    else:
        it_set.add(x['interest4'])
    if isinstance(x['interest5'], list):
        for num in x['interest5']:
            it_set.add(num)
    else:
        it_set.add(x['interest5'])


def cnt_topic(x):
    if isinstance(x['topic1'], list):
        for num in x['topic1']:
            it_set.add(num)
    else:
        it_set.add(x['topic1'])
    if isinstance(x['topic2'], list):
        for num in x['topic2']:
            it_set.add(num)
    else:
        it_set.add(x['topic2'])
    if isinstance(x['topic3'], list):
        for num in x['topic3']:
            it_set.add(num)
    else:
        it_set.add(x['topic3'])


def cnt_appAction(x):
    if isinstance(x['LBS'], list):
        for num in x['LBS']:
            it_set.add(num)
    else:
        it_set.add(x['LBS'])


# test = interest.apply(cnt_interest, axis=1)
df.apply(cnt_appAction, axis=1)
it_set.remove(np.nan)
it_list = list(it_set)
it_list.sort()
print(len(it_set))
print(it_list)
