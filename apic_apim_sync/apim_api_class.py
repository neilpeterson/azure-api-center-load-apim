from azure.identity import DefaultAzureCredential
from azure.mgmt.apimanagement import ApiManagementClient
import json
import requests

class apim_api():
    def __init__(self, apim_service):
        self.apim_service = apim_service

    def get_all_apis(self):

        """
        Gets all APIs from APIM and returns the API ID.
        """

        client = ApiManagementClient(
            credential = DefaultAzureCredential(), 
            subscription_id =self.apim_service.subscription_id
        )

        apim_apis = client.api.list_by_service(self.apim_service.resource_group_name, self.apim_service.name)
        return apim_apis
        