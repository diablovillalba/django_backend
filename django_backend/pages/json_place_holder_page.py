from end_points.set_up_end_points import *
from pages.base_page import Base_page

import jsonschema
import logging

LOGGER = logging.getLogger(__name__)
"""
Class to Page https://jsonplaceholder.typicode.com" get all resources get

"""
class Json_place_holder (Base_page):

    """
    Method to return the endpoint ready to use
    """
    def __init__(self):
        self.url_Basic = "https://jsonplaceholder.typicode.com"

    '''
    Method to get response of endpoint and get status
    '''
    def get_status_resource(self):

        end_point = Set_up_end_points(self.url_Basic)

        response = end_point.initialize_end_point()
        return response
    '''
    Method to get json response to verify json schema
    '''
    def get_validation_json_jsonSchema(self, json_file):
        validation = False
        try:
            response_json = self.get_response_json(self.url_Basic+json_file)
            file_schema = self.get_file_schema(json_file)
            jsonschema.validate(response_json,file_schema)
            validation = True
            return validation

        except jsonschema.exceptions.ValidationError as error:
            print("there is a error" + str(error))
            return validation
    '''
    Method to get information from resource by id or param
    '''
    def get_dicc_json_by_id(self, id, resource, param):
        LOGGER.info(self.url_Basic+"/"+resource+"/"+id)
        if param is not None:
            dicc_json = self.get_response_json(self.url_Basic + "/" + resource + "?" + param + "=" + id)
        else:
            dicc_json = self.get_response_json(self.url_Basic+"/"+resource+"/"+id)
        return dicc_json





