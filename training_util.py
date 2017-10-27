from pyexcel_ods import get_data
import json

data = get_data("data/training.ods")['Sheet1']
training = [{} for d in data if d]

i = 0
for d in data:
    if d:
        training[i]["class"] = str(d[0])
        training[i]["sentence"] = str(d[1])
        i += 1

training_file = "data/training-tan.json"
with open(training_file, 'w') as outfile:
    json.dump(training, outfile, indent=4)
