import json
import os
import numpy as np
from glob import glob
from IPython import embed
from tqdm import tqdm
root = "/mfs/home/limengwei/car_face/car_face/object_detection_network/data_both_side_single_day/JPEGFirst_Train/"
csv_label = open("train.csv","w")
filenames = glob(root+"/*/*.json")
filenames.sort()
np.random.shuffle(filenames)
image_format = "png"

def read_jsonfile(path):
    with open(path, "r", encoding='utf-8') as f:
        return json.load(f)
for json_file in tqdm(filenames):
    image_file = json_file.replace(".json",".%s"%image_format)
    obj = read_jsonfile(json_file)
    shapes = obj['shapes']
    for shape in shapes:
        label = shape["label"]
        x1 = shape["points"][0][0]
        y1 = shape["points"][0][1]
        x2 = shape["points"][1][0]
        y2 = shape["points"][1][1]
        x_min = min(x1, x2)
        x_max = max(x1, x2)
        y_min = min(y1, y2)
        y_max = max(y1, y2)
        csv_label.write(image_file+","+str(x_min)+","+str(y_min)+","+str(x_max)+","+str(y_max)+","+label+"\n")
        

