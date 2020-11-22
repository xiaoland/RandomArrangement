# 根据班级json文件进行随机摇号

import random
import json

# SETTINGS
number_limit = 1
reset = True
data_json_fp = "./json/2020_1_23_list.json"
pass_json_fp = "./json/ramdom_pass_index_list.json"

data = json.load(open(data_json_fp, "r", encoding="utf-8"))
data_keys = data.keys()
if reset:
    pass_data = []
else:
    pass_data = json.load(open(pass_json_fp, "r", encoding="utf-8"))


def random_pick():
    for i in range(0, number_limit):
        random_index = random.randint(1, len(data_keys))
        if random_index in pass_data:
            print("pass: ", random_index)
            continue
        else:
            pass_data.append(random_index)
            print(data[str(random_index)]["name"])


random_pick()
json.dump(pass_data, open(pass_json_fp, "w", encoding="utf-8"))
