"""convert json string to object"""
import json


def load_from_json_file(filename):
    """check the return"""
    with open(filename) as f:
        return json.loads(f.read())
