import json
import os
import glob
import unittest

def test_jsonfiles():
    json_files = glob.glob('./taxonomy/*.json')
    for file in json_files:
        yield validate_json_file, file


def validate_json_file(file):
    try:
        json.load(open(file,"r"))
    except ValueError as e:
        assert False, "Error in file: %s" % file