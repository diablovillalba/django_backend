from pages.json_place_holder_page import Json_place_holder
from http import HTTPStatus
import pytest
import logging

LOGGER = logging.getLogger(__name__)

# content of test_class.py
class TestClass_rest_back():
    '''
    Method to exercise 1
    get the resource to getting up the endpoint and send the httpStatus code
    '''


    def test_end_point_ok(self):
        place_holder = Json_place_holder()
        response_place_holder = place_holder.get_status_resource()
        assert response_place_holder.status_code == HTTPStatus.OK.value
    '''
    Method to exercise 2.1 Validate schema of json of response a resource vs file
    schema
    '''


    @pytest.mark.parametrize("json_file",[
        ("/posts"),
        ("/comments"),
        ("/albums"),
        ("/photos"),
        ("/todos"),
        ("/users")
    ])
    def test_validation_schema(self,json_file):
        place_holder = Json_place_holder()
        assert place_holder.get_validation_json_jsonSchema(json_file)==True


    '''
    function to get list of data provider 
    '''
    def get_data_to_provider(idToGet):

        if idToGet == "20":
            diccValuesHope = {'userId': 2,
                          'id': 20,
                          'title': "doloribus ad provident suscipit at",
                          'body': "qui consequuntur ducimus possimus quisquam amet similique\nsuscipit porro ipsam amet\neos veritatis officiis exercitationem vel fugit aut necessitatibus totam\nomnis rerum consequatur expedita quidem cumque explicabo"
                          }

        elif idToGet == "50":
            diccValuesHope = {'userId': 5,
                          'id': 50,
                          'title': "repellendus qui recusandae incidunt voluptates tenetur qui omnis exercitationem",
                          'body': "error suscipit maxime adipisci consequuntur recusandae\nvoluptas eligendi et est et voluptates\nquia distinctio ab amet quaerat molestiae et vitae\nadipisci impedit sequi nesciunt quis consectetur"
                          }

        elif idToGet == "100":
            diccValuesHope = {'userId': 10,
                          'id': 100,
                          'title': "at nam consequatur ea labore ea harum",
                          'body': "cupiditate quo est a modi nesciunt soluta\nipsa voluptas error itaque dicta in\nautem qui minus magnam et distinctio eum\naccusamus ratione error aut"
                          }

        return diccValuesHope

    '''
    Exercise 2.2 get by id (20,50,100)resources to post
    '''
    tuplaData = [["20", get_data_to_provider("20")],
                 ["50", get_data_to_provider("50")],
                 ["100", get_data_to_provider("100")]]
    @pytest.mark.parametrize("idToGet,data",tuplaData)
    def test_validation_data_by_id(self, idToGet, data):
        place_holder = Json_place_holder()
        assert place_holder.get_dicc_json_by_id(idToGet, "posts", None) == data


    '''
    Method to exercise 2.3 call resources with a common param
    '''
    tuplaData2= [["1", "posts", "userId"],
                 ["1", "comments", "postId"]]
    @pytest.mark.parametrize("id, resources, param",tuplaData2)
    def test_validation_resources_by_param_id(self, id, resources, param):
        place_holder = Json_place_holder()
        LOGGER.info("muestrame el len>>>>"+str(len(place_holder.get_dicc_json_by_id(id, resources, param))))
        assert len(place_holder.get_dicc_json_by_id(id, resources, param))!= 0


