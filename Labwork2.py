import json
import re
import math

data_file = open("../yelp_academic_dataset_review.json")
data = []

for line in data_file:
    data.append(json.loads(line)['text'])
    if len(data) == 10:
        break

data_file.close()


clusters = []
max_length = 0
for item in data:
    temp = []
    temp.append(len(item))
    max_length = max(len(item), max_length)
    clusters.append(((temp)))

def cal_dist(c1,c2):
    min_dist = max_length
    for i in c1:
        for j in c2:
            min_dist = min(min_dist, abs(i-j))
    return min_dist

while (len(clusters) > 3):
    coord = []
    min_dist = max_length
    for i in range(len(clusters)-1):
        for j in range(i+1, len(clusters)):
            distance = cal_dist(clusters[i],clusters[j])
            if distance < min_dist:
                coord = [i,j]
                min_dist = distance

    clusters[coord[0]] = clusters[coord[0]] + clusters[coord[1]]
    del clusters[coord[1]]
    print(coord)
    print(clusters)        
