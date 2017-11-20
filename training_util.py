from pyexcel_ods import get_data
import json

data = get_data("data/training-small.ods")['Sheet1']
training = [{} for d in data if d]

i = 0
for d in data:
    if d:
        training[i]["class"] = d[0].encode('utf-8')
        training[i]["sentence"] = d[1].encode('utf-8')
        i += 1

training_file = "data/training.json"
with open(training_file, 'w') as outfile:
    json.dump(training, outfile, indent=4)
