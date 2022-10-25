import json
from nltk.tokenize import word_tokenize
import re
import math

data_file = open("../yelp_academic_dataset_review.json")
data = []

for line in data_file:
    data.append(json.loads(line)['text'])
    if len(data) == 100000:
        break

data_file.close()


print(len(data))
print(data[1234])

def clean_non_english(txt):
    txt = re.sub(r'\W+', ' ', txt)
    txt = txt.lower()
    txt = txt.replace("[^a-zA-Z]", " ")
    word_tokens = word_tokenize(txt)
    filtered_word = [w for w in word_tokens if all(ord(c) < 128 for c in w)]
    filtered_word = [w + " " for w in filtered_word]
    return "".join(filtered_word)

for i in range(len(data)):
    data[i] = clean_non_english(data[i])
idf = {}
for line in data:
    line = line.strip()
    words = line.split()
    words = list(set(words))
    for word in words:
        if word not in idf:
            idf[word] = 1
        else:
            idf[word] +=1

for key in idf:
    idf[key] = idf[key]/len(data)
    idf[key] = math.log(1/idf[key])

tf_idf = []
for line in data:
    line = line.strip()
    words = line.split()
    temp_dict = {}
    for word in words:
        if word not in temp_dict:
            temp_dict[word] = 1
        else:
            temp_dict[word] +=1
    for key in temp_dict:
        temp_dict[key] = temp_dict[key] * idf[key]
    tf_idf.append(temp_dict)
print((tf_idf[1234]))