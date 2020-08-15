import yaml
import json

filename = "inventory.yaml"

with open(filename) as f:
    content = yaml.load(f)
print(json.dumps(content))

# if i want to configure json content on device terminal -
# load merge json terminal
# paste the configuration in json format &  ctrl+d
# show | compare
# commit
