import requests
import logging

LOGGER = logging.getLogger(__name__)
"""
Class to set up all necessaries endpoints
"""
class Set_up_end_points():

    def __init__(self, url):
        self.url=url
    '''
    Method to set up end point
    '''
    def initialize_end_point(self):
        response = requests.get(self.url)
        return response
