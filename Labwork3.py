import json
import re
import random
import math

data_file = open("../yelp_academic_dataset_review.json")
data = []

for line in data_file:
    data.append(json.loads(line)['text'])
    if len(data) == 1000:
        break

data_file.close()

num_clusters = 3
centroid_threshold = 0.005

clusters = []
centroid = []
items = []
centroid_diff = []
max_length = 0
for item in data:
    max_length = max(len(item), max_length)
    items.append(len(item))

for i in range(num_clusters):
    centroid.append(random.randint(0,max_length))
    centroid_diff.append(0)
print(centroid)
print(items)

def clusters_init():
    clus = []
    for i in range(num_clusters):
        clus.append([])
    return clus   

def choose_cl(point):
    min_dist = max_length
    cl = 0
    for i in range(num_clusters):
        dist = abs(point - centroid[i])
        if dist < min_dist:
            cl = i
            min_dist = dist
    return cl


while True:
    flag = 1
    clusters = clusters_init()
    for item in items: 
        clusters[choose_cl(item)].append(item)
    for i in range(num_clusters):
        temp = centroid[i]
        if len(clusters[i]) > 0:
            centroid[i] = sum(clusters[i])/len(clusters[i])
        centroid_diff[i] = abs(centroid[i] - temp)
        if centroid_diff[i] > centroid_threshold:
            flag = 0
    print(centroid)
    print(clusters)
    if flag:
        break

    

