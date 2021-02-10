import json
import sys

with open('config.json', 'r+') as f:
    data = json.load(f)
    data['version'] = sys.argv[1]

    f.seek(0)
    json.dump(data, f, indent=2)
    f.truncate()
