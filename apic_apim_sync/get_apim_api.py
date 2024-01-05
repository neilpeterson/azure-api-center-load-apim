from azure.identity import DefaultAzureCredential
from azure.mgmt.apimanagement import ApiManagementClient
import os

def get_apim_api(subcription_id, apim_resource_group_name, apim_name):

    """
    Returns a list of APIs from APIM with all properties.
    """

    client = ApiManagementClient(
        credential = DefaultAzureCredential(), 
        subscription_id = subcription_id
    )

    api = client.api.list_by_service(apim_resource_group_name, apim_name)

    return api
