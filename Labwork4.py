import json
import re
import random
import math

data_file = open("../yelp_academic_dataset_review.json")
data = []

for line in data_file:
    data.append(json.loads(line)['text'])
    if len(data) == 10:
        break

data_file.close()
items = []
bw = 20
for item in data:
    items.append(len(item))

def flat_kernel(x, bandwidth):
    return 1 if x < bandwidth else 0

def shiftMode(mode):
    newM = sum([xj*flat_kernel(xj-mode,bw) for xj in items]) 
    newN = sum([flat_kernel(xj-mode,bw) for xj in items])
    return newM/newN

threshold = 0.005
mode_list = []
clusters = []

for i in range(len(items)):
    k = 0
    old_mode = items[i]
    while True:
        newMode = shiftMode(old_mode)
        if abs(old_mode - newMode) < threshold:
            break
        else:
            old_mode = newMode
    mode_list.append(old_mode)


for mode in mode_list:
    if mode not in clusters:
        clusters += [mode]
print(mode_list)
print(clusters)


