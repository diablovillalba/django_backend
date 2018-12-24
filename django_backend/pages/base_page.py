import os
from urllib.request import urlopen
import json
import logging

LOGGER = logging.getLogger(__name__)
"""
Class base of all pages of project
"""
class Base_page():
    def __init__(self):
       pass
    '''
    Method to get data from json response
    '''
    def get_response_json(self,url):
        response = urlopen(url)
        json_data = response.read()
        json_data = json.loads(json_data)
        return (json_data)
    '''
    Method to get information from json_file to verify json schema
    '''
    def get_file_schema(self, json_file):
        dir_path = os.path.realpath("resources/"+json_file+".json")
        file_schema = open(dir_path, "r")
        json_file_schema = json.loads(file_schema.read())
        return json_file_schema