import json
import os
current_path = os.path.abspath(os.path.dirname(__file__))  # 返回当前文件路径
data_path = os.path.dirname(current_path)     # data文件夹路径
root_path = os.path.dirname(data_path)     # 根路径

json_path = root_path + '/personal.json'  # json文件的路径

with open(json_path, mode='r', encoding='utf8') as f:
    json_config = json.load(f)
    tushare_api = json_config['tushare_api']

